from enum import StrEnum


class RouteRegion(StrEnum):
    AMERICAS = "americas.api.riotgames.com"
    ASIA = "asia.api.riotgames.com"
    EUROPE = "europe.api.riotgames.com"
    SEA = "sea.api.riotgames.com"


class RoutePlatform(StrEnum):
    # America
    NA1 = "na1.api.riotgames.com"
    BR1 = "br1.api.riotgames.com"
    LA1 = "la1.api.riotgames.com"
    LA2 = "la2.api.riotgames.com"

    # Europe
    EUN1 = "eun1.api.riotgames.com"
    EUW1 = "euw1.api.riotgames.com"
    TR1 = "tr1.api.riotgames.com"
    RU = "ru.api.riotgames.com"

    # Asia
    JP1 = "jp1.api.riotgames.com"
    KR = "kr.api.riotgames.com"

    # SEA
    OC1 = "oc1.api.riotgames.com"
    SG2 = "sg2.api.riotgames.com"
    TW2 = "tw2.api.riotgames.com"
    VN2 = "vn2.api.riotgames.com"

    def to_region(self) -> RouteRegion:
        if self.name in ["NA1", "BR1", "LA1", "LA2"]:
            return RouteRegion.AMERICAS
        if self.name in ["EUN1", "EUW1", "TR1", "RU"]:
            return RouteRegion.EUROPE
        if self.name in ["JP1", "KR"]:
            return RouteRegion.ASIA
        if self.name in ["OC1", "SG2", "TW2", "VN2"]:
            return RouteRegion.SEA

        raise ValueError
