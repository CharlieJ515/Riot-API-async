import httpx


# riot_api/exceptions.py
class RiotAPIError(Exception):
    """Base class for all Riot API exceptions."""

    def __init__(self, status_code: int, headers: httpx.Headers, body: dict, msg: str):
        super().__init__(f"[{status_code}] {msg}")
        self.status_code = status_code
        self.headers = headers
        self.body = body
        self.msg = msg


class BadRequestError(RiotAPIError):
    """400 - Malformed request."""

    pass


class UnauthorizedError(RiotAPIError):
    """401 - Invalid API key."""

    pass


class ForbiddenError(RiotAPIError):
    """403 - Forbidden access."""

    pass


class NotFoundError(RiotAPIError):
    """404 - Resource not found."""

    pass


class RateLimitError(RiotAPIError):
    """429 - Too many requests."""

    def __init__(
        self,
        status_code: int,
        headers: httpx.Headers,
        body: str,
        msg: str,
        retry_after: int,
    ):
        super().__init__(status_code, headers, body, msg)
        self.retry_after = retry_after


class ServerError(RiotAPIError):
    """5xx - Server internal error."""

    pass
