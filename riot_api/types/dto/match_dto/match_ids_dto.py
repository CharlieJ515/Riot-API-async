from typing import List

from pydantic import RootModel


class MatchIdListDTO(RootModel):
    root: List[str]
