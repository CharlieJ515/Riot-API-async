from enum import IntEnum, StrEnum


class Participant(IntEnum):
    BLUE1 = 1
    BLUE2 = 2
    BLUE3 = 3
    BLUE4 = 4
    BLUE5 = 5
    RED1 = 6
    RED2 = 7
    RED3 = 8
    RED4 = 9
    RED5 = 10


class Team(IntEnum):
    BLUE = 100
    RED = 200


class Position(StrEnum):
    TOP = "TOP"
    JUNGLE = "JUNGLE"
    MIDDLE = "MIDDLE"
    BOTTOM = "BOTTOM"
    UTILITY = "UTILITY"


class KaynTransform(IntEnum):
    NONE = 0
    SLAYER = 1
    ASSASSIN = 2


class Role(StrEnum):
    SOLO = "SOLO"
    DUO = "DUO"
    SUPPORT = "SUPPORT"
    CARRY = "CARRY"
    NONE = "NONE"


class Lane(StrEnum):
    TOP = "TOP_LANE"
    MID = "MID_LANE"
    BOT = "BOT_LANE"
