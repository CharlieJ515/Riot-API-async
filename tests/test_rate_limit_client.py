import httpx
import pytest
import pytest_asyncio
import respx
import time

from pydantic import BaseModel
from limits.limits import RateLimitItem, RateLimitItemPerSecond
from limits.aio.storage import MemoryStorage

import riot_api
from riot_api.rate_limit_client import (
    reset_rate_limited_client,
    LimiterWithDecr,
    RateLimitExceeded,
    RateLimitClient,
)
from riot_api.types.request.routes import RouteRegion


ROUTE = RouteRegion.ASIA
PUUID = "l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w"


class DummyModel(BaseModel):
    value: int


def mock_get_account_by_puuid():
    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/riot/account/v1/accounts/by-puuid/l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w",
    ).mock(
        return_value=httpx.Response(
            200,
            json={"value": 123},
            headers={
                "X-App-Rate-Limit": "100:120,2:1",
                "X-Method-Rate-Limit": "50:10",
            },
        )
    )

    return route


@pytest_asyncio.fixture(autouse=True)
async def client():
    reset_rate_limited_client()
    client = RateLimitClient("api-key")
    yield client

    await client.close_session()


@pytest.mark.asyncio
@respx.mock
async def test_limit_info_extraction(client: RateLimitClient):
    route = mock_get_account_by_puuid()
    res, headers = await client.get_account_by_puuid(ROUTE, PUUID, DummyModel)

    expected_limits = {
        ("ASIA", "route_long"): RateLimitItemPerSecond(100 - 1, 120, "RIOT_API"),
        ("ASIA", "route_short"): RateLimitItemPerSecond(2 - 1, 1, "RIOT_API"),
        ("ASIA", "get_account_by_puuid"): RateLimitItemPerSecond(
            50 - 1, 10, "RIOT_API"
        ),
    }
    assert client.limits == expected_limits


@pytest.mark.asyncio
@respx.mock
async def test_rate_limit_exceeded(client: RateLimitClient):
    # reset_client()
    route = mock_get_account_by_puuid()
    res, headers = await client.get_account_by_puuid(ROUTE, PUUID, DummyModel)

    with pytest.raises(RateLimitExceeded) as limit_exceeded:
        res, headers = await client.get_account_by_puuid(ROUTE, PUUID, DummyModel)

    expected_retry_after = 1
    expected_reset_time = time.time() + expected_retry_after

    window = limit_exceeded.value.window_stat
    assert limit_exceeded.value.keys == ("ASIA", "route_short")
    assert limit_exceeded.value.retry_after == pytest.approx(expected_retry_after, 1e-2)
    assert window.remaining == 0
    assert window.reset_time == pytest.approx(expected_reset_time, 1e-2)

    keys = ("ASIA", "route_long")
    limits_long = client.limits.get(keys)
    assert limits_long is not None
    window_long = await client.limiter.get_window_stats(limits_long, *keys)
    assert window_long.remaining == limits_long.amount - 1

    keys = ("ASIA", "get_account_by_puuid")
    limits_endpoint = client.limits.get(keys)
    assert limits_endpoint is not None
    window_endpoint = await client.limiter.get_window_stats(limits_endpoint, *keys)
    assert window_endpoint.remaining == limits_endpoint.amount - 1


# @pytest.mark.asyncio
# async def test_first_call_sets_limit(rate_limit_client):
#     # Mock method: returns DummyModel + fake headers
#     async def fake_method(self, route):
#         return DummyModel(value=1), httpx.Headers({"X-Method-Rate-Limit": "10:1"})
#
#     # Decorate manually
#     decorated = add_limit(get_limit_info_endpoint, "test-endpoint")(fake_method)
#     RateLimitClient.test_method = decorated
#
#     # Call it
#     result, headers = await rate_limit_client.test_method(SimpleNamespace(name="KR"))
#
#     assert isinstance(result, DummyModel)
#     assert headers["X-Method-Rate-Limit"] == "10:1"
#
#
# @pytest.mark.asyncio
# async def test_limit_exceeded(rate_limit_client):
#     # Mock method to simulate always returning same headers
#     async def fake_method(self, route):
#         return DummyModel(value=1), httpx.Headers({"X-Method-Rate-Limit": "1:1"})
#
#     decorated = add_limit(get_limit_info_endpoint, "test-endpoint")(fake_method)
#     RateLimitClient.test_method = decorated
#
#     route = SimpleNamespace(name="KR")
#
#     # First call should pass
#     await rate_limit_client.test_method(route)
#
#     # Second call should exceed
#     with pytest.raises(RateLimitExceeded):
#         await rate_limit_client.test_method(route)
