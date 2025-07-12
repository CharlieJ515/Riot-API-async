from enum import StrEnum


class RankedTier(StrEnum):
    IRON = "IRON"
    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"
    EMERALD = "EMERALD"
    DIAMOND = "DIAMOND"
    MASTER = "MASTER"
    GRANDMASTER = "GRANDMASTER"
    CHALLENGER = "CHALLENGER"


class RankedDivision(StrEnum):
    I = "I"
    II = "II"
    III = "III"
    IV = "IV"


class RankedQueue(StrEnum):
    RANKED_SOLO_5x5 = "RANKED_SOLO_5x5"
    RANKED_FLEX_SR = "RANKED_FLEX_SR"
    RANKED_FLEX_TT = "RANKED_FLEX_TT"


class Account_v1(StrEnum):
    account_by_riot_id = "/riot/account/v1/accounts/by-riot-id/{gameName}/{tagLine}"
    account_by_puuid = "/riot/account/v1/accounts/by-puuid/{puuid}"
    account_region = "/riot/account/v1/region/by-game/{game}/by-puuid/{puuid}"


class Match_v5(StrEnum):
    match_by_puuid = "/lol/match/v5/matches/by-puuid/{puuid}/ids"
    match_by_matchId = "/lol/match/v5/matches/{matchId}"
    match_timeline = "/lol/match/v5/matches/{matchId}/timeline"


class League_v4(StrEnum):
    league_entry_by_tier = "/lol/league/v4/entries/{queue}/{tier}/{division}"
    league_by_leagueId = "/lol/league/v4/leagues/{leagueId}"
    challenger_league_by_queue = "/lol/league/v4/challengerleagues/by-queue/{queue}"
    grandmaster_league_by_queue = "/lol/league/v4/grandmasterleagues/by-queue/{queue}"
    master_league_by_queue = "/lol/league/v4/masterleagues/by-queue/{queue}"
