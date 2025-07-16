# riot_api/exceptions.py
class RiotAPIError(Exception):
    """Base class for all Riot API exceptions."""

    def __init__(self, status_code: int, message: str = ""):
        super().__init__(f"[{status_code}] {message}")
        self.status_code = status_code
        self.message = message


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

    def __init__(self, status_code: int, retry_after: float | None, message: str = ""):
        super().__init__(status_code, message)
        self.retry_after = retry_after


class ServerError(RiotAPIError):
    """5xx - Server internal error."""

    pass
