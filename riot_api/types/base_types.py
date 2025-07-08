from typing import NewType, Annotated
from datetime import datetime, timedelta

from pydantic import PlainValidator, PlainSerializer, Field

from riot_api.types.converters import (
    datetime_to_seconds,
    millis_to_datetime,
    datetime_to_millis,
    timedelta_to_seconds,
    millis_to_timedelta,
    timedelta_to_millis,
)

Puuid = NewType("Puuid", str)
Count = NewType("Count", int)
AmountInt = NewType("AmountInt", int)
AmountFloat = NewType("AmountFloat", float)
Percentage = NewType("Percentage", float)


Datetime = Annotated[datetime, PlainSerializer(datetime_to_seconds)]
DatetimeMilli = Annotated[
    datetime, PlainValidator(millis_to_datetime), PlainSerializer(datetime_to_millis)
]
TimeDelta = Annotated[timedelta, PlainSerializer(timedelta_to_seconds)]
TimeDeltaMilli = Annotated[
    timedelta, PlainValidator(millis_to_timedelta), PlainSerializer(timedelta_to_millis)
]
Unused = Field(
    exclude=True,
    repr=False,
    deprecated=True,
    description="Unused field",
)
