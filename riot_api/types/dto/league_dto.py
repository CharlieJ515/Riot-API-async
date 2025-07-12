from typing import List, Optional
from pydantic import RootModel

from riot_api.types.base_types import Puuid, AmountInt, Count
from riot_api.types.request import RankedQueue, RankedTier, RankedDivision
from riot_api.types.dto.base_model import BaseModelDTO


class LeagueListDTO(BaseModelDTO):
    leagueId: str
    entries: List["LeagueItemDTO"]
    tier: RankedTier
    name: str
    queue: RankedQueue


class LeagueItemDTO(BaseModelDTO):
    puuid: Puuid
    rank: RankedDivision
    leaguePoints: AmountInt
    wins: Count
    losses: Count
    freshBlood: bool
    inactive: bool
    veteran: bool
    hotStreak: bool
    miniSeries: Optional["MiniSeriesDTO"] = None


class LeagueEntryListDTO(RootModel):
    root: List["LeagueEntryDTO"]


class LeagueEntryDTO(BaseModelDTO):
    leagueId: str
    puuid: Puuid
    queueType: RankedQueue
    tier: RankedTier
    rank: RankedDivision
    leaguePoints: AmountInt
    wins: Count
    losses: Count
    hotStreak: bool
    veteran: bool
    freshBlood: bool
    inactive: bool
    miniSeries: Optional["MiniSeriesDTO"] = None


class MiniSeriesDTO(BaseModelDTO):
    losses: int
    progress: str
    target: int
    wins: int
