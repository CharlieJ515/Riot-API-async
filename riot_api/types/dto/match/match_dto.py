from typing import List, Optional, Annotated

from pydantic import Field, PlainValidator, PlainSerializer

from riot_api.types.enums import (
    ChampionId,
    ChampionName,
    ItemId,
    MapId,
)
from riot_api.types.enums import (
    Participant,
    Team,
    Position,
    KaynTransform,
    Role,
)
from riot_api.types.converters import normalize_champion_name
from riot_api.types.base_types import (
    Puuid,
    Count,
    AmountInt,
    AmountFloat,
    Percentage,
    DatetimeMilli,
    TimeDelta,
)
from riot_api.types.enums.summoner_spells import SummonerSpellId
from riot_api.types.dto.base_model import BaseModelDTO


class MatchDTO(BaseModelDTO):
    metadata: "MetadataDTO"
    info: "InfoDTO"


class MetadataDTO(BaseModelDTO):
    dataVersion: str
    matchId: str
    participants: List[Puuid]


class InfoDTO(BaseModelDTO):
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


class ParticipantDTO(BaseModelDTO):
    allInPings: Count
    assistMePings: Count
    assists: Count
    baronKills: Count
    bountyLevel: Optional[int] = None
    champExperience: AmountInt
    champLevel: Count
    championId: ChampionId
    championName: Annotated[
        ChampionName,
        PlainValidator(normalize_champion_name),
        PlainSerializer(lambda e: e.value, return_type=str),
    ]
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
    summoner1Id: SummonerSpellId
    summoner2Casts: Count
    summoner2Id: SummonerSpellId
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
    championSkinId: Optional[int] = None


class ChallengesDTO(BaseModelDTO):
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
    dancedWithRiftHerald: Count
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
    gameLength: TimeDelta
    getTakedownsInAllLanesEarlyJungleAsLaner: Optional[int] = None
    goldPerMinute: float
    hadOpenNexus: int
    immobilizeAndKillWithAlly: int
    initialBuffCount: Count
    initialCrabCount: Count
    jungleCsBefore10Minutes: float
    junglerTakedownsNearDamagedEpicMonster: Count
    kda: AmountFloat
    killAfterHiddenWithAlly: Count
    killedChampTookFullTeamDamageSurvived: int
    killingSprees: int
    killParticipation: Percentage
    killsNearEnemyTurret: Count
    killsOnOtherLanesEarlyJungleAsLaner: Optional[int] = None
    killsOnRecentlyHealedByAramPack: int
    killsUnderOwnTurret: int
    killsWithHelpFromEpicMonster: int
    knockEnemyIntoTeamAndKill: int
    kTurretsDestroyedBeforePlatesFall: int
    landSkillShotsEarlyGame: int
    laneMinionsFirst10Minutes: int
    lostAnInhibitor: Count
    maxKillDeficit: int
    mejaisFullStackInTime: int
    moreEnemyJungleThanOpponent: float
    multiKillOneSpell: Count
    multikills: Count
    multikillsAfterAggressiveFlash: Count
    multiTurretRiftHeraldCount: Count
    outerTurretExecutesBefore10Minutes: Count
    outnumberedKills: Count
    outnumberedNexusKill: Count
    perfectDragonSoulsTaken: int
    perfectGame: int
    pickKillWithAlly: int
    poroExplosions: int
    quickCleanse: int
    quickFirstTurret: int
    quickSoloKills: Count
    riftHeraldTakedowns: Count
    saveAllyFromDeath: Count
    scuttleCrabKills: Count
    shortestTimeToAceFromFirstTakedown: Optional[float] = None
    skillshotsDodged: int
    skillshotsHit: int
    snowballsHit: int
    soloBaronKills: Count
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
    soloKills: Count
    stealthWardsPlaced: Count
    survivedSingleDigitHpCount: Count
    survivedThreeImmobilizesInFight: int
    takedownOnFirstTurret: int
    takedowns: Count
    takedownsAfterGainingLevelAdvantage: int
    takedownsBeforeJungleMinionSpawn: Count
    takedownsFirstXMinutes: Count
    takedownsInAlcove: int
    takedownsInEnemyFountain: Count
    teamBaronKills: Count
    teamDamagePercentage: float
    teamElderDragonKills: Count
    teamRiftHeraldKills: Count
    tookLargeDamageSurvived: Count
    turretPlatesTaken: Count
    turretsTakenWithRiftHerald: Count
    turretTakedowns: Count
    twentyMinionsIn3SecondsCount: Count
    twoWardsOneSweeperCount: Count
    unseenRecalls: int
    visionScorePerMinute: AmountFloat
    wardsGuarded: Count
    wardTakedowns: Count
    wardTakedownsBefore20M: Count
    HealFromMapSources: AmountFloat


class MissionsDTO(BaseModelDTO):
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


class PerksDTO(BaseModelDTO):
    statPerks: "PerkStatsDTO"
    styles: List["PerkStyleDTO"]


class PerkStatsDTO(BaseModelDTO):
    defense: int
    flex: int
    offense: int


class PerkStyleDTO(BaseModelDTO):
    description: str
    selections: List["PerkStyleSelectionDTO"]
    style: int


class PerkStyleSelectionDTO(BaseModelDTO):
    perk: int
    var1: int
    var2: int
    var3: int


class TeamDTO(BaseModelDTO):
    bans: List["BanDTO"]
    objectives: "ObjectivesDTO"
    teamId: Team
    win: bool
    feats: "FeatsDTO"


class BanDTO(BaseModelDTO):
    championId: ChampionId
    pickTurn: int


class ObjectivesDTO(BaseModelDTO):
    baron: "ObjectiveDTO"
    champion: "ObjectiveDTO"
    dragon: "ObjectiveDTO"
    horde: "ObjectiveDTO"
    inhibitor: "ObjectiveDTO"
    riftHerald: "ObjectiveDTO"
    tower: "ObjectiveDTO"
    atakhan: "ObjectiveDTO"


class ObjectiveDTO(BaseModelDTO):
    first: bool
    kills: Count


class FeatsDTO(BaseModelDTO):
    EPIC_MONSTER_KILL: "FeatStateDTO"
    FIRST_BLOOD: "FeatStateDTO"
    FIRST_TURRET: "FeatStateDTO"


class FeatStateDTO(BaseModelDTO):
    featState: int
