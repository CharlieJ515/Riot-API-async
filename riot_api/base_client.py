from typing import TypeVar

from aiolimiter import AsyncLimiter
import httpx
from pydantic import BaseModel

from riot_api.types import HttpRequest, RateLimit

T = TypeVar("T", bound=BaseModel)


class BaseClient:
    def __init__(self, api_key: str, rate_limit: RateLimit):
        self.api_key = api_key
        self.limiter = AsyncLimiter(rate_limit.max_rate, rate_limit.time_period)
        self.session = httpx.AsyncClient()

    async def close(self) -> None:
        if not self.session.is_closed:
            await self.session.aclose()

    def deserialize(self, res: httpx.Response, response_model: type[T]) -> T:
        return response_model.model_validate_json(res.text)

    async def send_request(self, req: HttpRequest) -> BaseModel:
        if self.session.is_closed:
            raise RuntimeError("Session is already closed. Cannot send request.")

        async with self.limiter:
            # complete URL
            url = f"https://{req.route}{req.endpoint}"
            # authentication
            req.headers["X-Riot-Token"] = self.api_key

            res = await self.session.request(
                method=req.method.value,
                url=url,
                params=req.params,
                headers=req.headers,
                timeout=req.timeout,
            )

        return self.deserialize(res, req.response_model)
