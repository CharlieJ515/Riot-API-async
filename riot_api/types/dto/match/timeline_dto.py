from typing import List, Dict, Optional, Annotated, Literal, Union

from pydantic import (
    BaseModel,
    RootModel,
    Field,
    PlainSerializer,
    PlainValidator,
    ConfigDict,
)

from riot_api.types.base_types import (
    Count,
    AmountInt,
    Puuid,
    DatetimeMilli,
    TimeDeltaMilli,
)
from riot_api.types.enums import (
    Participant,
    Team,
    ItemId,
    Ward,
    ChampionName,
    Lane,
)
from riot_api.types.converters import parse_zero_as_none, serialize_none_as_zero

OptionalParticipant = Annotated[
    Optional[Participant],
    PlainValidator(parse_zero_as_none(Participant)),
    PlainSerializer(serialize_none_as_zero),
]


class TimelineDTO(BaseModel):
    metadata: "MetadataTimeLineDTO"
    info: "InfoTimeLineDTO"


class MetadataTimeLineDTO(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[Puuid]


class InfoTimeLineDTO(BaseModel):
    endOfGameResult: str
    frameInterval: TimeDeltaMilli
    gameId: int
    participants: List["ParticipantTimeLineDto"]
    frames: List["FramesTimeLineDto"]


class ParticipantTimeLineDto(BaseModel):
    participantId: Participant
    puuid: Puuid

    model_config = ConfigDict(use_enum_values=True)


class FramesTimeLineDto(BaseModel):
    events: List["EventsTimeLineDTO"]
    participantFrames: "ParticipantFramesDTO"
    timestamp: TimeDeltaMilli


#### EVENT START ####


class PauseEndEvent(BaseModel):
    type: Literal["PAUSE_END"]
    timestamp: TimeDeltaMilli
    realTimestamp: DatetimeMilli


class GameEndEvent(BaseModel):
    type: Literal["GAME_END"]
    timestamp: TimeDeltaMilli
    realTimestamp: DatetimeMilli
    gameId: int
    winningTeam: Team

    model_config = ConfigDict(use_enum_values=True)


class ItemPurchasedEvent(BaseModel):
    type: Literal["ITEM_PURCHASED"]
    timestamp: TimeDeltaMilli
    participantId: OptionalParticipant
    itemId: ItemId

    model_config = ConfigDict(use_enum_values=True)


class ItemDestroyedEvent(BaseModel):
    type: Literal["ITEM_DESTROYED"]
    timestamp: TimeDeltaMilli
    participantId: Participant
    itemId: ItemId

    model_config = ConfigDict(use_enum_values=True)


class ItemUndoEvent(BaseModel):
    type: Literal["ITEM_UNDO"]
    timestamp: TimeDeltaMilli
    participantId: Participant
    beforeId: ItemId
    afterId: ItemId
    goldGain: AmountInt

    model_config = ConfigDict(use_enum_values=True)


class ItemSoldEvent(BaseModel):
    type: Literal["ITEM_SOLD"]
    timestamp: TimeDeltaMilli
    participantId: Participant
    itemId: ItemId

    model_config = ConfigDict(use_enum_values=True)


class WardPlacedEvent(BaseModel):
    type: Literal["WARD_PLACED"]
    timestamp: TimeDeltaMilli
    creatorId: int
    wardType: Ward

    model_config = ConfigDict(use_enum_values=True)


class WardKillEvent(BaseModel):
    type: Literal["WARD_KILL"]
    timestamp: TimeDeltaMilli
    killerId: Participant
    wardType: Ward

    model_config = ConfigDict(use_enum_values=True)


class LevelUpEvent(BaseModel):
    type: Literal["LEVEL_UP"]
    timestamp: TimeDeltaMilli
    participantId: Participant
    level: Count

    model_config = ConfigDict(use_enum_values=True)


class SkillLevelUpEvent(BaseModel):
    type: Literal["SKILL_LEVEL_UP"]
    timestamp: TimeDeltaMilli
    participantId: Participant
    skillSlot: int
    levelUpType: str

    model_config = ConfigDict(use_enum_values=True)


class ObjectiveBountyPrestartEvent(BaseModel):
    type: Literal["OBJECTIVE_BOUNTY_PRESTART"]
    timestamp: TimeDeltaMilli
    actualStartTime: TimeDeltaMilli
    teamId: Team

    model_config = ConfigDict(use_enum_values=True)


class ChampionKillEvent(BaseModel):
    type: Literal["CHAMPION_KILL"]
    timestamp: TimeDeltaMilli
    bounty: AmountInt
    killStreakLength: Count
    killerId: Participant
    victimId: Participant
    position: "PositionDTO"
    shutdownBounty: int
    assistingParticipantIds: Optional[List[Participant]] = None
    victimDamageDealt: List["VictimDamageDTO"]
    victimDamageReceived: List["VictimDamageDTO"]

    model_config = ConfigDict(use_enum_values=True)


class VictimDamageDTO(BaseModel):
    basic: bool
    magicDamage: AmountInt
    physicalDamage: AmountInt
    spellName: str
    spellSlot: int
    trueDamage: AmountInt
    participantId: int
    name: str
    type: str


class ChampionSpecialKillEvent(BaseModel):
    type: Literal["CHAMPION_SPECIAL_KILL"]
    timestamp: TimeDeltaMilli
    killType: str
    multiKillLength: Optional[int] = None
    killerId: Participant
    position: "PositionDTO"

    model_config = ConfigDict(use_enum_values=True)


class TurretPlateDestroyedEvent(BaseModel):
    type: Literal["TURRET_PLATE_DESTROYED"]
    timestamp: TimeDeltaMilli
    teamId: Team
    killerId: OptionalParticipant
    laneType: Lane
    position: "PositionDTO"

    model_config = ConfigDict(use_enum_values=True)


class BuildingKillEvent(BaseModel):
    type: Literal["BUILDING_KILL"]
    timestamp: TimeDeltaMilli
    buildingType: str
    towerType: str
    teamId: Team
    killerId: Optional[Participant] = None
    assistingParticipantIds: Optional[List[Participant]] = None
    bounty: AmountInt
    laneType: Lane
    position: "PositionDTO"

    model_config = ConfigDict(use_enum_values=True)


class EliteMonsterKillEvent(BaseModel):
    type: Literal["ELITE_MONSTER_KILL"]
    timestamp: TimeDeltaMilli
    position: "PositionDTO"
    monsterType: str
    monsterSubType: Optional[str] = None
    killerId: Participant
    killerTeamId: Team
    bounty: AmountInt
    assistingParticipantIds: Optional[List[Participant]] = None

    model_config = ConfigDict(use_enum_values=True)


class DragonSoulGiven(BaseModel):
    type: Literal["DRAGON_SOUL_GIVEN"]
    timestamp: TimeDeltaMilli
    teamId: Literal[0]
    name: str


class FeatUpdateEvent(BaseModel):
    type: Literal["FEAT_UPDATE"]
    timestamp: TimeDeltaMilli
    featType: int
    featValue: int
    teamId: Team

    model_config = ConfigDict(use_enum_values=True)


EventsTimeLineDTO = Annotated[
    Union[
        PauseEndEvent,
        GameEndEvent,
        ItemPurchasedEvent,
        ItemDestroyedEvent,
        ItemUndoEvent,
        ItemSoldEvent,
        WardPlacedEvent,
        WardKillEvent,
        LevelUpEvent,
        SkillLevelUpEvent,
        ObjectiveBountyPrestartEvent,
        ChampionKillEvent,
        ChampionSpecialKillEvent,
        TurretPlateDestroyedEvent,
        BuildingKillEvent,
        EliteMonsterKillEvent,
        DragonSoulGiven,
        FeatUpdateEvent,
    ],
    Field(discriminator="type"),
]

#### EVENT END ####


class ParticipantFramesDTO(RootModel):
    root: Dict[Participant, "ParticipantFrameDTO"]

    model_config = ConfigDict(use_enum_values=True)


class ParticipantFrameDTO(BaseModel):
    championStats: "ChampionStatsDTO"
    currentGold: AmountInt
    damageStats: "DamageStatsDTO"
    goldPerSecond: AmountInt
    jungleMinionsKilled: int
    level: Count
    minionsKilled: int
    participantId: Participant
    position: "PositionDTO"
    timeEnemySpentControlled: int
    totalGold: AmountInt
    xp: int

    model_config = ConfigDict(use_enum_values=True)


class ChampionStatsDTO(BaseModel):
    abilityHaste: int
    abilityPower: int
    armor: int
    armorPen: int
    armorPenPercent: int
    attackDamage: int
    attackSpeed: int
    bonusArmorPenPercent: int
    bonusMagicPenPercent: int
    ccReduction: int
    cooldownReduction: int
    health: int
    healthMax: int
    healthRegen: int
    lifesteal: int
    magicPen: int
    magicPenPercent: int
    magicResist: int
    movementSpeed: int
    omnivamp: int
    physicalVamp: int
    power: int
    powerMax: int
    powerRegen: int
    spellVamp: int


class DamageStatsDTO(BaseModel):
    magicDamageDone: int
    magicDamageDoneToChampions: int
    magicDamageTaken: int
    physicalDamageDone: int
    physicalDamageDoneToChampions: int
    physicalDamageTaken: int
    totalDamageDone: int
    totalDamageDoneToChampions: int
    totalDamageTaken: int
    trueDamageDone: int
    trueDamageDoneToChampions: int
    trueDamageTaken: int


class PositionDTO(BaseModel):
    x: int
    y: int
