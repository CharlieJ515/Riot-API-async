from typing import Union, Optional, TypeVar, Type, cast, Tuple

from pydantic import BaseModel
import httpx

from riot_api.base_client import BaseClient
from riot_api.types.request import RoutePlatform, RouteRegion, HttpMethod, HttpRequest
from riot_api.types.request import (
    RankedTier,
    RankedDivision,
    RankedQueue,
    Account_v1,
    Match_v5,
    League_v4,
)
from riot_api.types.dto import (
    AccountDTO,
    AccountRegionDTO,
    LeagueListDTO,
    LeagueEntryListDTO,
    MatchDTO,
    TimelineDTO,
    MatchIdListDTO,
)


T = TypeVar("T", bound=BaseModel)


class Client(BaseClient):
    def __init__(self, api_key):
        super().__init__(api_key)

    # Account endpoints
    async def get_account_by_riot_id(
        self,
        route: RouteRegion,
        game_name: str,
        tag_line: str,
        response_model: Type[T] = AccountDTO,
    ) -> Tuple[T, httpx.Headers]:
        formatted_endpoint = Account_v1.account_by_riot_id.value.format(
            gameName=game_name, tagLine=tag_line
        )
        req = HttpRequest(
            method=HttpMethod.GET,
            route=route,
            endpoint=formatted_endpoint,
            response_model=response_model,
        )
        res, headers = await self.send_request(req)
        return cast(T, res), headers

    async def get_account_by_puuid(
        self,
        route: RouteRegion,
        puuid: str,
        response_model: Type[T] = AccountDTO,
    ) -> Tuple[T, httpx.Headers]:
        formatted_endpoint = Account_v1.account_by_puuid.value.format(puuid=puuid)
        req = HttpRequest(
            method=HttpMethod.GET,
            route=route,
            endpoint=formatted_endpoint,
            response_model=response_model,
        )
        res, headers = await self.send_request(req)
        return cast(T, res), headers

    async def get_account_region(
        self,
        route: Union[RouteRegion, RoutePlatform],
        game: str,
        puuid: str,
        response_model: Type[T] = AccountRegionDTO,
    ) -> Tuple[T, httpx.Headers]:
        formatted_endpoint = Account_v1.account_region.value.format(
            game=game, puuid=puuid
        )
        req = HttpRequest(
            method=HttpMethod.GET,
            route=route,
            endpoint=formatted_endpoint,
            response_model=response_model,
        )
        res, headers = await self.send_request(req)
        return cast(T, res), headers

    # Match endpoints
    async def get_match_ids_by_puuid(
        self,
        route: RouteRegion,
        puuid: str,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        queue: Optional[int] = None,
        type: Optional[str] = None,
        start: Optional[int] = None,
        count: Optional[int] = None,
        response_model: Type[T] = MatchIdListDTO,
    ) -> Tuple[T, httpx.Headers]:
        """
        Retrieve a list of match IDs for a given PUUID with optional filters.

        Parameters:
            route (RouteRegion): Platform route.
            puuid (str): Player UUID.

            startTime (Optional[int]): Epoch timestamp in seconds. The matchlist started storing timestamps on June 16th, 2021.
                Any matches played before this date won't be included if the startTime filter is set.

            endTime (Optional[int]): Epoch timestamp in seconds.

            queue (Optional[int]): Filter the match IDs by specific queue ID.
                This filter is mutually inclusive with 'type' filter—matches must match both filters.

            type (Optional[str]): Filter the match IDs by match type.
                This filter is mutually inclusive with 'queue' filter—matches must match both filters.

            start (Optional[int]): Defaults to 0. Start index for pagination.

            count (Optional[int]): Defaults to 20. Valid range: 0 to 100. Number of match IDs to return.

        Returns:
            The response from the Riot API as a deserialized JSON object.
        """
        formatted_endpoint = Match_v5.match_by_puuid.value.format(puuid=puuid)

        # Build query dict from non-None parameters
        params = {
            k: v
            for k, v in {
                "startTime": startTime,
                "endTime": endTime,
                "queue": queue,
                "type": type,
                "start": start,
                "count": count,
            }.items()
            if v is not None
        }

        req = HttpRequest(
            method=HttpMethod.GET,
            route=route,
            endpoint=formatted_endpoint,
            params=params,
            response_model=response_model,
        )
        res, headers = await self.send_request(req)
        return cast(T, res), headers

    async def get_match_by_match_id(
        self, route: RouteRegion, match_id: str, response_model: Type[T] = MatchDTO
    ) -> Tuple[T, httpx.Headers]:
        formatted_endpoint = Match_v5.match_by_matchId.value.format(matchId=match_id)
        req = HttpRequest(
            method=HttpMethod.GET,
            route=route,
            endpoint=formatted_endpoint,
            response_model=response_model,
        )
        res, headers = await self.send_request(req)
        return cast(T, res), headers

    async def get_match_timeline(
        self, route: RouteRegion, match_id: str, response_model: Type[T] = TimelineDTO
    ) -> Tuple[T, httpx.Headers]:
        formatted_endpoint = Match_v5.match_timeline.value.format(matchId=match_id)
        req = HttpRequest(
            method=HttpMethod.GET,
            route=route,
            endpoint=formatted_endpoint,
            response_model=response_model,
        )
        res, headers = await self.send_request(req)
        return cast(T, res), headers

    # League endpoints
    async def get_league_entries_by_tier(
        self,
        route: RoutePlatform,
        queue: RankedQueue,
        tier: RankedTier,
        division: RankedDivision,
        page: int = 1,
        response_model: Type[T] = LeagueEntryListDTO,
    ) -> Tuple[T, httpx.Headers]:
        formatted_endpoint = League_v4.league_entry_by_tier.value.format(
            queue=queue.value, tier=tier.value, division=division.value
        )
        req = HttpRequest(
            method=HttpMethod.GET,
            route=route,
            endpoint=formatted_endpoint,
            params={"page": page},
            response_model=response_model,
        )
        res, headers = await self.send_request(req)
        return cast(T, res), headers

    async def get_league_by_league_id(
        self,
        route: RoutePlatform,
        league_id: str,
        response_model: Type[T] = LeagueListDTO,
    ) -> Tuple[T, httpx.Headers]:
        formatted_endpoint = League_v4.league_by_leagueId.value.format(
            leagueId=league_id
        )
        req = HttpRequest(
            method=HttpMethod.GET,
            route=route,
            endpoint=formatted_endpoint,
            response_model=response_model,
        )
        res, headers = await self.send_request(req)
        return cast(T, res), headers

    async def get_challenger_league(
        self,
        route: RoutePlatform,
        queue: RankedQueue,
        response_model: Type[T] = LeagueListDTO,
    ) -> Tuple[T, httpx.Headers]:
        formatted_endpoint = League_v4.challenger_league_by_queue.value.format(
            queue=queue.value
        )
        req = HttpRequest(
            method=HttpMethod.GET,
            route=route,
            endpoint=formatted_endpoint,
            response_model=response_model,
        )
        res, headers = await self.send_request(req)
        return cast(T, res), headers

    async def get_grandmaster_league(
        self,
        route: RoutePlatform,
        queue: RankedQueue,
        response_model: Type[T] = LeagueListDTO,
    ) -> Tuple[T, httpx.Headers]:
        formatted_endpoint = League_v4.grandmaster_league_by_queue.value.format(
            queue=queue.value
        )
        req = HttpRequest(
            method=HttpMethod.GET,
            route=route,
            endpoint=formatted_endpoint,
            response_model=response_model,
        )
        res, headers = await self.send_request(req)
        return cast(T, res), headers

    async def get_master_league(
        self,
        route: RoutePlatform,
        queue: RankedQueue,
        response_model: Type[T] = LeagueListDTO,
    ) -> Tuple[T, httpx.Headers]:
        formatted_endpoint = League_v4.master_league_by_queue.value.format(
            queue=queue.value
        )
        req = HttpRequest(
            method=HttpMethod.GET,
            route=route,
            endpoint=formatted_endpoint,
            response_model=response_model,
        )
        res, headers = await self.send_request(req)
        return cast(T, res), headers
