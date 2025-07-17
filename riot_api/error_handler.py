from typing import Optional
from httpx import Response, head
from riot_api.exceptions import (
    RiotAPIError,
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    NotFoundError,
    RateLimitError,
    ServerError,
)

ERROR_MAP = {
    400: BadRequestError,
    401: UnauthorizedError,
    403: ForbiddenError,
    404: NotFoundError,
    429: RateLimitError,
}


def check_status_code(res: Response) -> None:
    if res.status_code < 400:
        return

    status_code = res.status_code
    headers = res.headers
    body = res.json()
    msg = body.get("status", {}).get("message", res.text.strip())
    cls = ERROR_MAP.get(res.status_code, RiotAPIError)

    if res.status_code == 429:
        retry_after: int = int(res.headers["retry-after"])
        raise cls(status_code, headers, body, msg, retry_after)

    elif 500 <= res.status_code < 600:
        raise ServerError(status_code, headers, body, msg)
    else:
        raise cls(status_code, headers, body, msg)
