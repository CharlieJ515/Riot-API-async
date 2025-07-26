import inspect
from typing import (
    Awaitable,
    Callable,
    cast,
    Tuple,
    TypeVar,
    ParamSpec,
    Concatenate,
    Optional,
)
import asyncio
import functools
import time
from datetime import datetime, timezone


import httpx
from pydantic import BaseModel
from limits.limits import RateLimitItem, RateLimitItemPerSecond
from limits.util import WindowStats
from limits.aio.storage import MemoryStorage
from limits.aio.strategies import FixedWindowRateLimiter

from riot_api.client import Client
from riot_api.types.request import HttpRequest
from riot_api.types.request.routes import RouteRegion, RoutePlatform


class RateLimitExceeded(Exception):
    def __init__(self, keys: tuple[str, ...], window_stat: WindowStats):
        self.keys = keys
        self.window_stat = window_stat
        now = time.time()
        self.retry_after = max(0, window_stat.reset_time - now)

        key_str = ":".join(keys)
        reset_dt = datetime.fromtimestamp(window_stat.reset_time, tz=timezone.utc)
        reset_str = reset_dt.isoformat()

        message = (
            f"Rate limit exceeded for '{key_str}': "
            f"{window_stat.remaining} remaining; resets in {self.retry_after:.2f} seconds "
            f"(at {reset_str} UTC)."
        )
        super().__init__(message)


class LimiterWithDecr(FixedWindowRateLimiter):
    def __init__(self, storage: MemoryStorage):
        super().__init__(storage)

    async def decr(self, item: RateLimitItem, *identifiers: str, cost: int = 1):
        await self.storage.decr(  # type: ignore[reportAttributeAccessIssue]
            item.key_for(*identifiers),
            amount=cost,
        )


P = ParamSpec("P")
RequestFunc = Callable[P, Awaitable[tuple[BaseModel, httpx.Headers]]]
RequestMethod = Callable[
    Concatenate["RateLimitClient", P], Awaitable[Tuple[BaseModel, httpx.Headers]]
]


def add_limit(
    get_limit_info: Callable[[httpx.Headers], RateLimitItem],
    limit_key: str,
    weight: int = 1,
) -> Callable[[RequestMethod[P]], RequestFunc[P]]:
    assert weight > 0, "Weight must be a positive integer"

    def decorator(func: RequestMethod[P]) -> RequestFunc[P]:
        sig = inspect.signature(func)

        block = asyncio.Event()
        wake = asyncio.Event()

        @functools.wraps(func)
        async def wrapper(
            self: "RateLimitClient", *args: P.args, **kwargs: P.kwargs
        ) -> tuple[BaseModel, httpx.Headers]:
            nonlocal block, wake

            bound = sig.bind(self, *args, **kwargs)
            bound.apply_defaults()

            # get keys
            route: RouteRegion | RoutePlatform
            req: Optional[HttpRequest] = bound.arguments.get("req")
            if req:
                route = req.route
            else:
                value = bound.arguments.get("region") or bound.arguments.get("platform")
                if value is None:
                    raise ValueError("No region/platform found in arguments")
                route = value
            route_key = route.name
            keys = (route_key, limit_key)

            limit = self.limits.get(keys)
            if limit is None:
                if not block.is_set():
                    block.set()

                    res, headers = await func(self, *args, **kwargs)
                    limit = get_limit_info(headers)
                    self.limits[keys] = limit

                    wake.set()
                    await self.limiter.hit(limit, *keys, cost=weight)
                    return res, headers

                else:
                    print("waiting for limit")
                    await wake.wait()
                    limit = self.limits.get(keys)
                    if limit is None:
                        raise ValueError("")

            available = await self.limiter.hit(limit, *keys, cost=weight)
            if not available:
                window_stat = await self.limiter.get_window_stats(limit, *keys)
                raise RateLimitExceeded(keys, window_stat)

            try:
                res, headers = await func(self, *args, **kwargs)
            except RateLimitExceeded as e:
                await self.limiter.decr(limit, *keys, cost=weight)
                raise e

            return res, headers

        return cast(RequestFunc[P], wrapper)

    return decorator


class RateLimitClient(Client):
    limits: dict[tuple[str, str], RateLimitItem] = {}
    storage: MemoryStorage
    limiter: LimiterWithDecr


def get_limit_info_endpoint(headers: httpx.Headers) -> RateLimitItem:
    limit_str = headers["X-Method-Rate-Limit"].split(":")
    amount, multiples = int(limit_str[0]) - 1, int(limit_str[1])

    return RateLimitItemPerSecond(amount, multiples, "RIOT_API")


def get_limit_info_route_long(headers: httpx.Headers) -> RateLimitItem:
    limit_str = headers["X-App-Rate-Limit"].split(",")[0].split(":")
    amount, multiples = int(limit_str[0]) - 1, int(limit_str[1])

    return RateLimitItemPerSecond(amount, multiples, "RIOT_API")


def get_limit_info_route_short(headers: httpx.Headers) -> RateLimitItem:
    limit_str = headers["X-App-Rate-Limit"].split(",")[1].split(":")
    amount, multiples = int(limit_str[0]) - 1, int(limit_str[1])

    return RateLimitItemPerSecond(amount, multiples, "RIOT_API")


def reset_rate_limited_client():
    # initialize limits, storage, limiter
    storage = MemoryStorage()
    RateLimitClient.storage = storage
    RateLimitClient.limiter = LimiterWithDecr(storage)
    RateLimitClient.limits.clear()

    # apply rate limit to endpoints
    endpoint_methods = [
        # Account endpoints
        "get_account_by_riot_id",
        "get_account_by_puuid",
        "get_account_region",
        # Match endpoints
        "get_match_ids_by_puuid",
        "get_match_by_match_id",
        "get_match_timeline",
        # League endpoints
        "get_league_entries_by_tier",
        "get_league_by_league_id",
        "get_challenger_league",
        "get_grandmaster_league",
        "get_master_league",
    ]
    for name in endpoint_methods:
        method = getattr(Client, name)
        limited_method = add_limit(get_limit_info_endpoint, name)(method)
        setattr(RateLimitClient, name, limited_method)

    route_methods = ["send_request"]
    for name in route_methods:
        method = getattr(Client, name)
        limited_method_long = add_limit(get_limit_info_route_long, "route_long")(method)
        limited_method_short = add_limit(get_limit_info_route_short, "route_short")(
            limited_method_long
        )
        setattr(RateLimitClient, name, limited_method_short)


reset_rate_limited_client()
