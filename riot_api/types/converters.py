from datetime import datetime, timedelta
import re


from riot_api.types.enums import ChampionName


def normalize_string(s: str) -> str:
    """remove non-alphabetic characters then lowercase"""
    return re.sub(r"[^a-zA-Z]", "", s).lower()


def datetime_to_millis(dt: datetime) -> int:
    return int(dt.timestamp() * 1000)


def millis_to_datetime(v: int) -> datetime:
    return datetime.fromtimestamp(v / 1000)


def timedelta_to_seconds(td: timedelta) -> int:
    return int(td.total_seconds())


def normalize_champion_name(v: str) -> str:
    normalized_str = normalize_string(v)
    return ChampionName(normalized_str)
