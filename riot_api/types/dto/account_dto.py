from pydantic import BaseModel


class AccountDTO(BaseModel):
    puuid: str
    gameName: str
    tagLine: str


class AccountRegionDTO(BaseModel):
    puuid: str
    game: str
    region: str
