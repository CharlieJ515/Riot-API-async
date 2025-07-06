from enum import Enum
from dataclasses import dataclass, field
from typing import Union, Dict, Optional, Any, Type

from pydantic import BaseModel

from riot_api.types.region import RoutePlatform, RouteRegion


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"


@dataclass
class HttpRequest:
    method: HttpMethod
    route: Union[RoutePlatform, RouteRegion]
    endpoint: str
    response_model: type[BaseModel]
    params: Dict[str, Any] = field(default_factory=dict)
    headers: Dict[str, str] = field(default_factory=dict)
    timeout: Optional[float] = 3.0


@dataclass
class RateLimit:
    max_rate: int
    time_period: int
