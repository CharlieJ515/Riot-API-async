from typing import List, Optional, NewType, Annotated
from datetime import datetime, timedelta
from enum import Enum, IntEnum, StrEnum
import re

from pydantic import BaseModel, Field, PlainValidator, ConfigDict, PlainSerializer

from riot_api.types.league_of_legends import (
    ChampionId,
    ChampionName,
    ItemId,
    SummonerSpell,
)
from riot_api.types.riot import MapId


def datetime_to_millis(dt: datetime) -> int:
    return int(dt.timestamp() * 1000)


def millis_to_datetime(v: int) -> datetime:
    return datetime.fromtimestamp(v / 1000)


def timedelta_to_seconds(td: timedelta) -> int:
    return int(td.total_seconds())


def normalize_champion_name(v: str) -> str:
    cleaned = re.sub(r"[^A-Za-z]", "", v).lower()
    return ChampionName(cleaned)


DatetimeMilli = Annotated[
    datetime, PlainValidator(millis_to_datetime), PlainSerializer(datetime_to_millis)
]
TimeDelta = Annotated[timedelta, PlainSerializer(timedelta_to_seconds)]
Puuid = NewType("Puuid", str)
Count = NewType("Count", int)
AmountInt = NewType("AmountInt", int)
AmountFloat = NewType("AmountFloat", float)
Percentage = NewType("Percentage", float)
Unused = Field(
    exclude=True,
    repr=False,
    deprecated=True,
    description="Unused field",
)


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


class MatchDTO(BaseModel):
    metadata: "MetadataDTO"
    info: "InfoDTO"


class MetadataDTO(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[Puuid]


class InfoDTO(BaseModel):
    endOfGameResult: str
    gameCreation: DatetimeMilli
    # TODO - change gameDuration according to riot document
    gameDuration: TimeDelta
    gameEndTimestamp: DatetimeMilli
    gameId: int
    gameMode: str
    gameName: str
    gameStartTimestamp: DatetimeMilli
    gameType: str
    gameVersion: str
    mapId: MapId
    participants: List["ParticipantDTO"]
    platformId: str
    queueId: int
    teams: List["TeamDTO"]
    tournamentCode: Optional[str] = None

    model_config = ConfigDict(use_enum_values=True)


class ParticipantDTO(BaseModel):
    allInPings: Count
    assistMePings: Count
    assists: Count
    baronKills: Count
    bountyLevel: Optional[int] = None
    champExperience: AmountInt
    champLevel: Count
    championId: ChampionId
    championName: Annotated[ChampionName, PlainValidator(normalize_champion_name)]
    commandPings: Count
    championTransform: KaynTransform
    consumablesPurchased: Count
    challenges: "ChallengesDTO"
    damageDealtToBuildings: AmountInt
    damageDealtToObjectives: AmountInt
    damageDealtToTurrets: AmountInt
    damageSelfMitigated: AmountInt
    deaths: Count
    detectorWardsPlaced: Count
    doubleKills: Count
    dragonKills: Count
    eligibleForProgression: bool
    enemyMissingPings: Count
    enemyVisionPings: Count
    firstBloodAssist: bool
    firstBloodKill: bool
    firstTowerAssist: bool
    firstTowerKill: bool
    gameEndedInEarlySurrender: bool
    gameEndedInSurrender: bool
    holdPings: Count
    getBackPings: Count
    goldEarned: AmountInt
    goldSpent: AmountInt
    individualPosition: Position
    inhibitorKills: Count
    inhibitorTakedowns: Count
    inhibitorsLost: Count
    item0: ItemId
    item1: ItemId
    item2: ItemId
    item3: ItemId
    item4: ItemId
    item5: ItemId
    item6: ItemId
    itemsPurchased: Count
    killingSprees: Count
    kills: Count
    lane: Position
    largestCriticalStrike: AmountInt
    largestKillingSpree: Count
    largestMultiKill: Count
    longestTimeSpentLiving: TimeDelta
    magicDamageDealt: AmountInt
    magicDamageDealtToChampions: AmountInt
    magicDamageTaken: AmountInt
    missions: "MissionsDTO"
    neutralMinionsKilled: Count
    needVisionPings: Count
    nexusKills: Count
    nexusTakedowns: Count
    nexusLost: Count
    objectivesStolen: Count
    objectivesStolenAssists: Count
    onMyWayPings: Count
    participantId: Participant
    PlayerScore0: int
    PlayerScore1: int
    PlayerScore2: int
    PlayerScore3: int
    PlayerScore4: int
    PlayerScore5: int
    PlayerScore6: int
    PlayerScore7: int
    PlayerScore8: int
    PlayerScore9: int
    PlayerScore10: int
    PlayerScore11: int
    pentaKills: Count
    perks: "PerksDTO"
    physicalDamageDealt: AmountInt
    physicalDamageDealtToChampions: AmountInt
    physicalDamageTaken: AmountInt
    placement: int
    playerAugment1: int
    playerAugment2: int
    playerAugment3: int
    playerAugment4: int
    playerAugment5: int
    playerAugment6: int
    playerSubteamId: int
    pushPings: Count
    profileIcon: int
    puuid: Puuid
    quadraKills: Count
    riotIdGameName: str
    riotIdTagline: str
    role: Role
    sightWardsBoughtInGame: Count
    spell1Casts: Count
    spell2Casts: Count
    spell3Casts: Count
    spell4Casts: Count
    subteamPlacement: int
    summoner1Casts: Count
    summoner1Id: SummonerSpell
    summoner2Casts: Count
    summoner2Id: SummonerSpell
    summonerId: str
    summonerLevel: int
    summonerName: str
    teamEarlySurrendered: bool
    teamId: Team
    teamPosition: Position
    timeCCingOthers: AmountInt
    timePlayed: TimeDelta
    totalAllyJungleMinionsKilled: Count
    totalDamageDealt: AmountInt
    totalDamageDealtToChampions: AmountInt
    totalDamageShieldedOnTeammates: AmountInt
    totalDamageTaken: AmountInt
    totalEnemyJungleMinionsKilled: Count
    totalHeal: AmountInt
    totalHealsOnTeammates: AmountInt
    totalMinionsKilled: Count
    totalTimeCCDealt: int
    totalTimeSpentDead: TimeDelta
    totalUnitsHealed: AmountInt
    tripleKills: Count
    trueDamageDealt: AmountInt
    trueDamageDealtToChampions: AmountInt
    trueDamageTaken: AmountInt
    turretKills: Count
    turretTakedowns: Count
    turretsLost: Count
    unrealKills: Count
    visionScore: AmountInt
    visionClearedPings: Count
    visionWardsBoughtInGame: Count
    wardsKilled: Count
    wardsPlaced: Count
    win: bool
    basicPings: Count
    dangerPings: Count
    retreatPings: Count
    championSkinId: int

    model_config = ConfigDict(use_enum_values=True)


class ChallengesDTO(BaseModel):
    assistStreakCount12: int = Field(alias="12AssistStreakCount")
    baronBuffGoldAdvantageOverThreshold: Optional[int] = None
    controlWardTimeCoverageInRiverOrEnemyHalf: Optional[float] = None
    earliestBaron: Optional[int] = None
    earliestDragonTakedown: Optional[float] = None
    earliestElderDragon: Optional[int] = None
    earlyLaningPhaseGoldExpAdvantage: int
    fasterSupportQuestCompletion: Optional[int] = None
    fastestLegendary: Optional[float] = None
    hadAfkTeammate: Optional[int] = None
    highestChampionDamage: Optional[int] = None
    highestCrowdControlScore: Optional[int] = None
    highestWardKills: Optional[int] = None
    junglerKillsEarlyJungle: Optional[int] = None
    killsOnLanersEarlyJungleAsJungler: Optional[int] = None
    laningPhaseGoldExpAdvantage: int
    legendaryCount: int
    maxCsAdvantageOnLaneOpponent: float
    maxLevelLeadLaneOpponent: int
    mostWardsDestroyedOneSweeper: Optional[int] = None
    mythicItemUsed: Optional[int] = None
    playedChampSelectPosition: int
    soloTurretsLategame: Optional[int] = None
    takedownsFirst25Minutes: Optional[int] = None
    teleportTakedowns: Optional[int] = None
    thirdInhibitorDestroyedTime: Optional[int] = None
    threeWardsOneSweeperCount: Optional[int] = None
    visionScoreAdvantageLaneOpponent: float
    InfernalScalePickup: int
    fistBumpParticipation: int
    voidMonsterKill: Count
    abilityUses: Count
    acesBefore15Minutes: Count
    alliedJungleMonsterKills: float
    baronTakedowns: Count
    blastConeOppositeOpponentCount: Count
    bountyGold: float
    buffsStolen: Count
    completeSupportQuestInTime: int
    controlWardsPlaced: Count
    damagePerMinute: float
    damageTakenOnTeamPercentage: Percentage
    dancedWithRiftHerald: int
    deathsByEnemyChamps: Count
    dodgeSkillShotsSmallWindow: Count
    doubleAces: Count
    dragonTakedowns: Count
    legendaryItemUsed: List[ItemId]
    effectiveHealAndShielding: float
    elderDragonKillsWithOpposingSoul: int
    elderDragonMultikills: Count
    enemyChampionImmobilizations: int
    enemyJungleMonsterKills: float
    epicMonsterKillsNearEnemyJungler: int
    epicMonsterKillsWithin30SecondsOfSpawn: int
    epicMonsterSteals: Count
    epicMonsterStolenWithoutSmite: int
    firstTurretKilled: int
    firstTurretKilledTime: Optional[float] = None
    flawlessAces: int
    fullTeamTakedown: int
    gameLength: float
    getTakedownsInAllLanesEarlyJungleAsLaner: Optional[int] = None
    goldPerMinute: float
    hadOpenNexus: int
    immobilizeAndKillWithAlly: int
    initialBuffCount: Count
    initialCrabCount: Count
    jungleCsBefore10Minutes: float
    junglerTakedownsNearDamagedEpicMonster: int
    kda: float
    killAfterHiddenWithAlly: int
    killedChampTookFullTeamDamageSurvived: int
    killingSprees: int
    killParticipation: float
    killsNearEnemyTurret: int
    killsOnOtherLanesEarlyJungleAsLaner: Optional[int] = None
    killsOnRecentlyHealedByAramPack: int
    killsUnderOwnTurret: int
    killsWithHelpFromEpicMonster: int
    knockEnemyIntoTeamAndKill: int
    kTurretsDestroyedBeforePlatesFall: int
    landSkillShotsEarlyGame: int
    laneMinionsFirst10Minutes: int
    lostAnInhibitor: int
    maxKillDeficit: int
    mejaisFullStackInTime: int
    moreEnemyJungleThanOpponent: float
    multiKillOneSpell: int
    multikills: int
    multikillsAfterAggressiveFlash: int
    multiTurretRiftHeraldCount: int
    outerTurretExecutesBefore10Minutes: int
    outnumberedKills: int
    outnumberedNexusKill: int
    perfectDragonSoulsTaken: int
    perfectGame: int
    pickKillWithAlly: int
    poroExplosions: int
    quickCleanse: int
    quickFirstTurret: int
    quickSoloKills: int
    riftHeraldTakedowns: int
    saveAllyFromDeath: int
    scuttleCrabKills: int
    shortestTimeToAceFromFirstTakedown: Optional[float] = None
    skillshotsDodged: int
    skillshotsHit: int
    snowballsHit: int
    soloBaronKills: int
    SWARM_DefeatAatrox: int
    SWARM_DefeatBriar: int
    SWARM_DefeatMiniBosses: int
    SWARM_EvolveWeapon: int
    SWARM_Have3Passives: int
    SWARM_KillEnemy: int
    SWARM_PickupGold: float
    SWARM_ReachLevel50: int
    SWARM_Survive15Min: int
    SWARM_WinWith5EvolvedWeapons: int
    soloKills: int
    stealthWardsPlaced: int
    survivedSingleDigitHpCount: int
    survivedThreeImmobilizesInFight: int
    takedownOnFirstTurret: int
    takedowns: int
    takedownsAfterGainingLevelAdvantage: int
    takedownsBeforeJungleMinionSpawn: int
    takedownsFirstXMinutes: int
    takedownsInAlcove: int
    takedownsInEnemyFountain: int
    teamBaronKills: int
    teamDamagePercentage: float
    teamElderDragonKills: int
    teamRiftHeraldKills: int
    tookLargeDamageSurvived: int
    turretPlatesTaken: int
    turretsTakenWithRiftHerald: int
    turretTakedowns: int
    twentyMinionsIn3SecondsCount: int
    twoWardsOneSweeperCount: int
    unseenRecalls: int
    visionScorePerMinute: float
    wardsGuarded: int
    wardTakedowns: int
    wardTakedownsBefore20M: int
    HealFromMapSources: float

    model_config = ConfigDict(use_enum_values=True)


class MissionsDTO(BaseModel):
    playerScore0: int
    playerScore1: int
    playerScore2: int
    playerScore3: int
    playerScore4: int
    playerScore5: int
    playerScore6: int
    playerScore7: int
    playerScore8: int
    playerScore9: int
    playerScore10: int
    playerScore11: int


class PerksDTO(BaseModel):
    statPerks: "PerkStatsDTO"
    styles: List["PerkStyleDTO"]


class PerkStatsDTO(BaseModel):
    defense: int
    flex: int
    offense: int


class PerkStyleDTO(BaseModel):
    description: str
    selections: List["PerkStyleSelectionDTO"]
    style: int


class PerkStyleSelectionDTO(BaseModel):
    perk: int
    var1: int
    var2: int
    var3: int


class TeamDTO(BaseModel):
    bans: List["BanDTO"]
    objectives: "ObjectivesDTO"
    teamId: int
    win: bool
    feats: "FeatsDTO"


class BanDTO(BaseModel):
    championId: ChampionId
    pickTurn: int


class ObjectivesDTO(BaseModel):
    baron: "ObjectiveDTO"
    champion: "ObjectiveDTO"
    dragon: "ObjectiveDTO"
    horde: "ObjectiveDTO"
    inhibitor: "ObjectiveDTO"
    riftHerald: "ObjectiveDTO"
    tower: "ObjectiveDTO"
    atakhan: "ObjectiveDTO"


class ObjectiveDTO(BaseModel):
    first: bool
    kills: Count


class FeatsDTO(BaseModel):
    EPIC_MONSTER_KILL: "FeatStateDTO"
    FIRST_BLOOD: "FeatStateDTO"
    FIRST_TURRET: "FeatStateDTO"


class FeatStateDTO(BaseModel):
    featState: int
