from typing import List, Dict, Optional, Annotated, Literal, Union

from pydantic import (
    RootModel,
    Field,
    PlainSerializer,
    PlainValidator,
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
from riot_api.types.dto.base_model import BaseModelDTO

OptionalParticipant = Annotated[
    Optional[Participant],
    PlainValidator(parse_zero_as_none(Participant)),
    PlainSerializer(serialize_none_as_zero),
]


class TimelineDTO(BaseModelDTO):
    metadata: "MetadataTimeLineDTO"
    info: "InfoTimeLineDTO"


class MetadataTimeLineDTO(BaseModelDTO):
    dataVersion: str
    matchId: str
    participants: List[Puuid]


class InfoTimeLineDTO(BaseModelDTO):
    endOfGameResult: str
    frameInterval: TimeDeltaMilli
    gameId: int
    participants: List["ParticipantTimeLineDto"]
    frames: List["FramesTimeLineDto"]


class ParticipantTimeLineDto(BaseModelDTO):
    participantId: Participant
    puuid: Puuid


class FramesTimeLineDto(BaseModelDTO):
    events: List["EventsTimeLineDTO"]
    participantFrames: "ParticipantFramesDTO"
    timestamp: TimeDeltaMilli


#### EVENT START ####


class PauseEndEvent(BaseModelDTO):
    type: Literal["PAUSE_END"]
    timestamp: TimeDeltaMilli
    realTimestamp: DatetimeMilli


class GameEndEvent(BaseModelDTO):
    type: Literal["GAME_END"]
    timestamp: TimeDeltaMilli
    realTimestamp: DatetimeMilli
    gameId: int
    winningTeam: Team


class ItemPurchasedEvent(BaseModelDTO):
    type: Literal["ITEM_PURCHASED"]
    timestamp: TimeDeltaMilli
    participantId: OptionalParticipant
    itemId: ItemId


class ItemDestroyedEvent(BaseModelDTO):
    type: Literal["ITEM_DESTROYED"]
    timestamp: TimeDeltaMilli
    participantId: Participant
    itemId: ItemId


class ItemUndoEvent(BaseModelDTO):
    type: Literal["ITEM_UNDO"]
    timestamp: TimeDeltaMilli
    participantId: Participant
    beforeId: ItemId
    afterId: ItemId
    goldGain: AmountInt


class ItemSoldEvent(BaseModelDTO):
    type: Literal["ITEM_SOLD"]
    timestamp: TimeDeltaMilli
    participantId: Participant
    itemId: ItemId


class WardPlacedEvent(BaseModelDTO):
    type: Literal["WARD_PLACED"]
    timestamp: TimeDeltaMilli
    creatorId: int
    wardType: Ward


class WardKillEvent(BaseModelDTO):
    type: Literal["WARD_KILL"]
    timestamp: TimeDeltaMilli
    killerId: Participant
    wardType: Ward


class LevelUpEvent(BaseModelDTO):
    type: Literal["LEVEL_UP"]
    timestamp: TimeDeltaMilli
    participantId: Participant
    level: Count


class SkillLevelUpEvent(BaseModelDTO):
    type: Literal["SKILL_LEVEL_UP"]
    timestamp: TimeDeltaMilli
    participantId: Participant
    skillSlot: int
    levelUpType: str


class ObjectiveBountyPrestartEvent(BaseModelDTO):
    type: Literal["OBJECTIVE_BOUNTY_PRESTART"]
    timestamp: TimeDeltaMilli
    actualStartTime: TimeDeltaMilli
    teamId: Team


class ChampionKillEvent(BaseModelDTO):
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


class VictimDamageDTO(BaseModelDTO):
    basic: bool
    magicDamage: AmountInt
    physicalDamage: AmountInt
    spellName: str
    spellSlot: int
    trueDamage: AmountInt
    participantId: int
    name: str
    type: str


class ChampionSpecialKillEvent(BaseModelDTO):
    type: Literal["CHAMPION_SPECIAL_KILL"]
    timestamp: TimeDeltaMilli
    killType: str
    multiKillLength: Optional[int] = None
    killerId: Participant
    position: "PositionDTO"


class TurretPlateDestroyedEvent(BaseModelDTO):
    type: Literal["TURRET_PLATE_DESTROYED"]
    timestamp: TimeDeltaMilli
    teamId: Team
    killerId: OptionalParticipant
    laneType: Lane
    position: "PositionDTO"


class BuildingKillEvent(BaseModelDTO):
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


class EliteMonsterKillEvent(BaseModelDTO):
    type: Literal["ELITE_MONSTER_KILL"]
    timestamp: TimeDeltaMilli
    position: "PositionDTO"
    monsterType: str
    monsterSubType: Optional[str] = None
    killerId: Participant
    killerTeamId: Team
    bounty: AmountInt
    assistingParticipantIds: Optional[List[Participant]] = None


class DragonSoulGiven(BaseModelDTO):
    type: Literal["DRAGON_SOUL_GIVEN"]
    timestamp: TimeDeltaMilli
    teamId: Literal[0]
    name: str


class FeatUpdateEvent(BaseModelDTO):
    type: Literal["FEAT_UPDATE"]
    timestamp: TimeDeltaMilli
    featType: int
    featValue: int
    teamId: Team


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


class ParticipantFrameDTO(BaseModelDTO):
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


class ChampionStatsDTO(BaseModelDTO):
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


class DamageStatsDTO(BaseModelDTO):
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


class PositionDTO(BaseModelDTO):
    x: int
    y: int
