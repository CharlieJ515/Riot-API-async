from typing import List, Dict, Optional, Annotated, Literal, Union
from pydantic import BaseModel, RootModel, Field


class TimelineDTO(BaseModel):
    metadata: "MetadataTimeLineDTO"
    info: "InfoTimeLineDTO"


class MetadataTimeLineDTO(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[str]


class InfoTimeLineDTO(BaseModel):
    endOfGameResult: str
    frameInterval: int
    gameId: int
    participants: List["ParticipantTimeLineDto"]
    frames: List["FramesTimeLineDto"]


class ParticipantTimeLineDto(BaseModel):
    participantId: int
    puuid: str


class FramesTimeLineDto(BaseModel):
    events: List["EventsTimeLineDTO"]
    participantFrames: "ParticipantFramesDTO"
    timestamp: int


#### EVENT START ####


class PauseEndEvent(BaseModel):
    type: Literal["PAUSE_END"]
    timestamp: int
    realTimestamp: int


class GameEndEvent(BaseModel):
    type: Literal["GAME_END"]
    timestamp: int
    realTimestamp: int
    gameId: int
    winningTeam: int


class ItemPurchasedEvent(BaseModel):
    type: Literal["ITEM_PURCHASED"]
    timestamp: int
    participantId: int
    itemId: int


class ItemDestroyedEvent(BaseModel):
    type: Literal["ITEM_DESTROYED"]
    timestamp: int
    participantId: int
    itemId: int


class ItemUndoEvent(BaseModel):
    type: Literal["ITEM_UNDO"]
    timestamp: int
    participantId: int
    beforeId: int
    afterId: int
    goldGain: int


class ItemSoldEvent(BaseModel):
    type: Literal["ITEM_SOLD"]
    timestamp: int
    participantId: int
    itemId: int


class WardPlacedEvent(BaseModel):
    type: Literal["WARD_PLACED"]
    timestamp: int
    creatorId: int
    wardType: str


class WardKillEvent(BaseModel):
    type: Literal["WARD_KILL"]
    timestamp: int
    killerId: int
    wardType: str


class LevelUpEvent(BaseModel):
    type: Literal["LEVEL_UP"]
    timestamp: int
    participantId: int
    level: int


class SkillLevelUpEvent(BaseModel):
    type: Literal["SKILL_LEVEL_UP"]
    timestamp: int
    participantId: int
    skillSlot: int
    levelUpType: str


class ObjectiveBountyPrestartEvent(BaseModel):
    type: Literal["OBJECTIVE_BOUNTY_PRESTART"]
    timestamp: int
    actualStartTime: int
    teamId: int


class ChampionKillEvent(BaseModel):
    type: Literal["CHAMPION_KILL"]
    timestamp: int
    bounty: int
    killStreakLength: int
    killerId: int
    victimId: int
    position: "PositionDTO"
    shutdownBounty: int
    assistingParticipantIds: Optional[List[int]] = None
    victimDamageDealt: List["VictimDamageDTO"]
    victimDamageReceived: List["VictimDamageDTO"]


class VictimDamageDTO(BaseModel):
    basic: bool
    magicDamage: int
    name: str
    participantId: int
    physicalDamage: int
    spellName: str
    spellSlot: int
    trueDamage: int
    type: str


class ChampionSpecialKillEvent(BaseModel):
    type: Literal["CHAMPION_SPECIAL_KILL"]
    timestamp: int
    killType: str
    multiKillLength: Optional[int] = None
    killerId: int
    position: "PositionDTO"


class TurretPlateDestroyedEvent(BaseModel):
    type: Literal["TURRET_PLATE_DESTROYED"]
    timestamp: int
    teamId: int
    killerId: Optional[int] = None
    laneType: str
    position: "PositionDTO"


class BuildingKillEvent(BaseModel):
    type: Literal["BUILDING_KILL"]
    timestamp: int
    buildingType: str
    towerType: str
    teamId: int
    killerId: Optional[int] = None
    assistingParticipantIds: Optional[List[int]] = None
    bounty: Optional[int] = None
    laneType: str
    laneType: str
    position: "PositionDTO"


class EliteMonsterKillEvent(BaseModel):
    type: Literal["ELITE_MONSTER_KILL"]
    timestamp: int
    position: "PositionDTO"
    monsterType: str
    monsterSubType: Optional[str] = None
    killerId: int
    killerTeamId: int
    bounty: int
    assistingParticipantIds: Optional[List[int]] = None


class DragonSoulGiven(BaseModel):
    type: Literal["DRAGON_SOUL_GIVEN"]
    timestamp: int
    teamId: int
    name: str


class FeatUpdateEvent(BaseModel):
    type: Literal["FEAT_UPDATE"]
    timestamp: int
    featType: int
    featValue: int
    teamId: int


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
    root: Dict[str, "ParticipantFrameDTO"]


class ParticipantFrameDTO(BaseModel):
    championStats: "ChampionStatsDTO"
    currentGold: int
    damageStats: "DamageStatsDTO"
    goldPerSecond: int
    jungleMinionsKilled: int
    level: int
    minionsKilled: int
    participantId: int
    position: "PositionDTO"
    timeEnemySpentControlled: int
    totalGold: int
    xp: int


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
