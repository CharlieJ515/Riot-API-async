from pydantic import BaseModel

from riot_api.types.base_types import Puuid


class AccountDTO(BaseModel):
    puuid: Puuid
    gameName: str
    tagLine: str


class AccountRegionDTO(BaseModel):
    puuid: Puuid
    game: str
    region: str
