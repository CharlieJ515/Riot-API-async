from typing import List, Optional
from pydantic import BaseModel, RootModel

from riot_api.types.base_types import Puuid


class LeagueListDTO(BaseModel):
    leagueId: str
    entries: List["LeagueItemDTO"]
    tier: str
    name: str
    queue: str


class LeagueItemDTO(BaseModel):
    freshBlood: bool
    wins: int
    miniSeries: Optional["MiniSeriesDTO"] = None
    inactive: bool
    veteran: bool
    hotStreak: bool
    rank: str
    leaguePoints: int
    losses: int
    puuid: Puuid


class LeagueEntryListDTO(RootModel):
    root: List["LeagueEntryDTO"]


class LeagueEntryDTO(BaseModel):
    leagueId: str
    puuid: Puuid
    queueType: str
    tier: str
    rank: str
    leaguePoints: int
    wins: int
    losses: int
    hotStreak: bool
    veteran: bool
    freshBlood: bool
    inactive: bool
    miniSeries: Optional["MiniSeriesDTO"] = None


class MiniSeriesDTO(BaseModel):
    losses: int
    progress: str
    target: int
    wins: int
