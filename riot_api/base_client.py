from typing import TypeVar, Tuple

import httpx
from pydantic import BaseModel

from riot_api.types.request import HttpRequest
from riot_api.error_handler import check_status_code

T = TypeVar("T", bound=BaseModel)


class BaseClient:
    _shared_session: httpx.AsyncClient | None = None

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session = httpx.AsyncClient()

    @classmethod
    def get_session(cls) -> httpx.AsyncClient:
        if cls._shared_session is None or cls._shared_session.is_closed:
            cls._shared_session = httpx.AsyncClient(http2=True)
        return cls._shared_session

    @classmethod
    async def close_session(cls) -> None:
        if cls._shared_session and not cls._shared_session.is_closed:
            await cls._shared_session.aclose()
            cls._shared_session = None

    def deserialize(self, res: httpx.Response, response_model: type[T]) -> T:
        return response_model.model_validate_json(res.text)

    async def send_request(self, req: HttpRequest) -> Tuple[BaseModel, httpx.Headers]:
        session = self.get_session()

        # complete URL
        url = f"https://{req.route}{req.endpoint}"
        # authentication
        req.headers["X-Riot-Token"] = self.api_key

        res = await session.request(
            method=req.method.value,
            url=url,
            params=req.params,
            headers=req.headers,
            timeout=req.timeout,
        )
        check_status_code(res)

        return self.deserialize(res, req.response_model), res.headers
