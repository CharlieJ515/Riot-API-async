from riot_api.types.base_types import Puuid
from riot_api.types.dto.base_model import BaseModelDTO


class AccountDTO(BaseModelDTO):
    puuid: Puuid
    gameName: str
    tagLine: str


class AccountRegionDTO(BaseModelDTO):
    puuid: Puuid
    game: str
    region: str
