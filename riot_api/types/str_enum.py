from enum import Enum


class StrEnum(Enum):
    def __str__(self) -> str:
        return str(self.value)
