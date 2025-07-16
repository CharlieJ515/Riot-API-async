from typing import Optional
from httpx import Response
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

    body = res.json()
    msg = body.get("status", {}).get("message", res.text.strip())
    cls = ERROR_MAP.get(res.status_code, RiotAPIError)

    if res.status_code == 429:
        retry_after: Optional[float] = None
        if "Retry-After" in res.headers:
            try:
                retry_after = float(res.headers["Retry-After"])
            except ValueError:
                pass
        raise cls(res.status_code, retry_after, msg)

    elif 500 <= res.status_code < 600:
        raise ServerError(res.status_code, msg)
    else:
        raise cls(res.status_code, msg)
