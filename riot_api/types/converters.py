from datetime import datetime, timedelta
from typing import TypeVar, Type, Optional
from enum import IntEnum
import re


from riot_api.types.enums import ChampionName

# nullable int
T = TypeVar("T", bound=IntEnum)


def parse_zero_as_none(enum_cls: Type[T]):
    def parser(v: int | None) -> Optional[T]:
        if v in (0, None):
            return None
        return enum_cls(v)

    return parser


def serialize_none_as_zero(v: Optional[T]) -> int:
    return 0 if v is None else v.value


# string
def normalize_string(s: str) -> str:
    """remove non-alphabetic characters then lowercase"""
    return re.sub(r"[^a-zA-Z]", "", s).lower()


def normalize_champion_name(v: str) -> str:
    normalized_str = normalize_string(v)
    return ChampionName(normalized_str)


# datetime
def datetime_to_seconds(dt: datetime) -> int:
    return int(dt.timestamp())


def datetime_to_millis(dt: datetime) -> int:
    return int(dt.timestamp() * 1000)


def millis_to_datetime(v: int) -> datetime:
    return datetime.fromtimestamp(v / 1000)


# timedelta
def timedelta_to_seconds(td: timedelta) -> int:
    return int(td.total_seconds())


def millis_to_timedelta(v: int | float) -> timedelta:
    return timedelta(milliseconds=v)


def timedelta_to_millis(td: timedelta) -> int:
    return int(td.total_seconds() * 1000)
