from typing import List, Optional
from pydantic import BaseModel, Field


class MatchDTO(BaseModel):
    metadata: "MetadataDTO"
    info: "InfoDTO"


class MetadataDTO(BaseModel):
    dataVersion: str
    matchId: str
    participants: List[str]


class InfoDTO(BaseModel):
    endOfGameResult: str
    gameCreation: int
    gameDuration: int
    gameEndTimestamp: int
    gameId: int
    gameMode: str
    gameName: str
    gameStartTimestamp: int
    gameType: str
    gameVersion: str
    mapId: int
    participants: List["ParticipantDTO"]
    platformId: str
    queueId: int
    teams: List["TeamDTO"]
    tournamentCode: Optional[str] = None


class ParticipantDTO(BaseModel):
    allInPings: int
    assistMePings: int
    assists: int
    baronKills: int
    bountyLevel: Optional[int] = None
    champExperience: int
    champLevel: int
    championId: int
    championName: str
    commandPings: int
    championTransform: int
    consumablesPurchased: int
    challenges: "ChallengesDTO"
    damageDealtToBuildings: int
    damageDealtToObjectives: int
    damageDealtToTurrets: int
    damageSelfMitigated: int
    deaths: int
    detectorWardsPlaced: int
    doubleKills: int
    dragonKills: int
    eligibleForProgression: bool
    enemyMissingPings: int
    enemyVisionPings: int
    firstBloodAssist: bool
    firstBloodKill: bool
    firstTowerAssist: bool
    firstTowerKill: bool
    gameEndedInEarlySurrender: bool
    gameEndedInSurrender: bool
    holdPings: int
    getBackPings: int
    goldEarned: int
    goldSpent: int
    individualPosition: str
    inhibitorKills: int
    inhibitorTakedowns: int
    inhibitorsLost: int
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    itemsPurchased: int
    killingSprees: int
    kills: int
    lane: str
    largestCriticalStrike: int
    largestKillingSpree: int
    largestMultiKill: int
    longestTimeSpentLiving: int
    magicDamageDealt: int
    magicDamageDealtToChampions: int
    magicDamageTaken: int
    missions: "MissionsDTO"
    neutralMinionsKilled: int
    needVisionPings: int
    nexusKills: int
    nexusTakedowns: int
    nexusLost: int
    objectivesStolen: int
    objectivesStolenAssists: int
    onMyWayPings: int
    participantId: int
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
    pentaKills: int
    perks: "PerksDTO"
    physicalDamageDealt: int
    physicalDamageDealtToChampions: int
    physicalDamageTaken: int
    placement: int
    playerAugment1: int
    playerAugment2: int
    playerAugment3: int
    playerAugment4: int
    playerAugment5: int
    playerAugment6: int
    playerSubteamId: int
    pushPings: int
    profileIcon: int
    puuid: str
    quadraKills: int
    riotIdGameName: str
    riotIdTagline: str
    role: str
    sightWardsBoughtInGame: int
    spell1Casts: int
    spell2Casts: int
    spell3Casts: int
    spell4Casts: int
    subteamPlacement: int
    summoner1Casts: int
    summoner1Id: int
    summoner2Casts: int
    summoner2Id: int
    summonerId: str
    summonerLevel: int
    summonerName: str
    teamEarlySurrendered: bool
    teamId: int
    teamPosition: str
    timeCCingOthers: int
    timePlayed: int
    totalAllyJungleMinionsKilled: int
    totalDamageDealt: int
    totalDamageDealtToChampions: int
    totalDamageShieldedOnTeammates: int
    totalDamageTaken: int
    totalEnemyJungleMinionsKilled: int
    totalHeal: int
    totalHealsOnTeammates: int
    totalMinionsKilled: int
    totalTimeCCDealt: int
    totalTimeSpentDead: int
    totalUnitsHealed: int
    tripleKills: int
    trueDamageDealt: int
    trueDamageDealtToChampions: int
    trueDamageTaken: int
    turretKills: int
    turretTakedowns: int
    turretsLost: int
    unrealKills: int
    visionScore: int
    visionClearedPings: int
    visionWardsBoughtInGame: int
    wardsKilled: int
    wardsPlaced: int
    win: bool
    basicPings: int
    dangerPings: int
    retreatPings: int
    championSkinId: int


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
    voidMonsterKill: int
    abilityUses: int
    acesBefore15Minutes: int
    alliedJungleMonsterKills: float
    baronTakedowns: int
    blastConeOppositeOpponentCount: int
    bountyGold: float
    buffsStolen: int
    completeSupportQuestInTime: int
    controlWardsPlaced: int
    damagePerMinute: float
    damageTakenOnTeamPercentage: float
    dancedWithRiftHerald: int
    deathsByEnemyChamps: int
    dodgeSkillShotsSmallWindow: int
    doubleAces: int
    dragonTakedowns: int
    legendaryItemUsed: List[int]
    effectiveHealAndShielding: float
    elderDragonKillsWithOpposingSoul: int
    elderDragonMultikills: int
    enemyChampionImmobilizations: int
    enemyJungleMonsterKills: float
    epicMonsterKillsNearEnemyJungler: int
    epicMonsterKillsWithin30SecondsOfSpawn: int
    epicMonsterSteals: int
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
    initialBuffCount: int
    initialCrabCount: int
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
    championId: int
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
    kills: int


class FeatsDTO(BaseModel):
    EPIC_MONSTER_KILL: "FeatStateDTO"
    FIRST_BLOOD: "FeatStateDTO"
    FIRST_TURRET: "FeatStateDTO"


class FeatStateDTO(BaseModel):
    featState: int

