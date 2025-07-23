import os

import httpx
import respx
import pytest
import pytest_asyncio
from conftest import load_test_json

from riot_api.client import Client


@pytest_asyncio.fixture
async def client():
    api_key = os.environ.get("RIOT_API_KEY", "")
    client = Client(api_key=api_key)
    yield client

    await client.close_session()


@pytest.mark.asyncio
@respx.mock
async def test_get_account_by_riot_id(client: Client):
    from riot_api.types.request import RouteRegion
    from riot_api.types.dto import AccountDTO

    ROUTE_REGION = RouteRegion.ASIA
    GAME_NAME = "summer"
    TAG_LINE = "pado"

    json_str = load_test_json("get_account_by_riot_id.json")
    expected_response = AccountDTO.model_validate_json(json_str)

    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/riot/account/v1/accounts/by-riot-id/summer/pado",
    ).mock(return_value=httpx.Response(200, content=json_str))

    response, headers = await client.get_account_by_riot_id(
        ROUTE_REGION, GAME_NAME, TAG_LINE
    )

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_account_by_puuid(client: Client):
    from riot_api.types.request import RouteRegion
    from riot_api.types.dto import AccountDTO

    ROUTE_REGION = RouteRegion.ASIA
    PUUID = (
        "l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w"
    )

    json_str = load_test_json("get_account_by_puuid.json")
    expected_response = AccountDTO.model_validate_json(json_str)
    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/riot/account/v1/accounts/by-puuid/l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response, headers = await client.get_account_by_puuid(ROUTE_REGION, PUUID)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_account_region(client: Client):
    from riot_api.types.request import RouteRegion
    from riot_api.types.dto import AccountRegionDTO

    ROUTE_REGION = RouteRegion.ASIA
    PUUID = (
        "l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w"
    )

    json_str = load_test_json("get_account_region.json")
    expected_response = AccountRegionDTO.model_validate_json(json_str)

    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/riot/account/v1/region/by-game/lol/by-puuid/l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response, headers = await client.get_account_region(ROUTE_REGION, "lol", PUUID)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_match_by_match_id(client: Client):
    from riot_api.types.request import RouteRegion
    from riot_api.types.dto import MatchDTO

    ROUTE_REGION = RouteRegion.ASIA
    MATCH_ID = "KR_7692293629"

    json_str = load_test_json("get_match_by_match_id.json")
    expected_response = MatchDTO.model_validate_json(json_str)

    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/lol/match/v5/matches/KR_7692293629",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response, headers = await client.get_match_by_match_id(ROUTE_REGION, MATCH_ID)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.skip(reason="response not ready")
@pytest.mark.asyncio
@respx.mock
async def test_get_match_ids_by_puuid(client: Client):
    from riot_api.types.request import RouteRegion
    from riot_api.types.dto import MatchIdListDTO

    ROUTE_REGION = RouteRegion.ASIA
    PUUID = (
        "l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w"
    )

    json_str = load_test_json("get_match_ids_by_puuid.json")
    expected_response = MatchIdListDTO.model_validate_json(json_str)

    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/lol/match/v5/matches/by-puuid/l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w/ids",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response, headers = await client.get_match_ids_by_puuid(ROUTE_REGION, PUUID)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_match_timeline(client: Client):
    from riot_api.types.request import RouteRegion
    from riot_api.types.dto import TimelineDTO

    ROUTE_REGION = RouteRegion.ASIA
    MATCH_ID = "KR_7692293629"

    json_str = load_test_json("get_match_timeline.json")
    expected_response = TimelineDTO.model_validate_json(json_str)

    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/lol/match/v5/matches/KR_7692293629/timeline",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response, headers = await client.get_match_timeline(ROUTE_REGION, MATCH_ID)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_league_entry_by_tier(client: Client):
    from riot_api.types.request import (
        RankedTier,
        RankedDivision,
        RankedQueue,
        RoutePlatform,
    )
    from riot_api.types.dto import LeagueEntryListDTO

    ROUTE_PLATFORM = RoutePlatform.KR
    QUEUE = RankedQueue.RANKED_SOLO_5x5
    TIER = RankedTier.DIAMOND
    DIVISION = RankedDivision.I
    PAGE = 3

    json_str = load_test_json("get_league_entry_by_tier.json")
    expected_response = LeagueEntryListDTO.model_validate_json(json_str)

    route = respx.route(
        method="GET",
        host="kr.api.riotgames.com",
        path="/lol/league/v4/entries/RANKED_SOLO_5x5/DIAMOND/I",
        params={"page": PAGE},
    ).mock(return_value=httpx.Response(200, content=json_str))
    response, headers = await client.get_league_entries_by_tier(
        ROUTE_PLATFORM,
        QUEUE,
        TIER,
        DIVISION,
        PAGE,
    )

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_league_by_league_id(client: Client):
    from riot_api.types.request import RoutePlatform
    from riot_api.types.dto import LeagueListDTO

    ROUTE_PLATFORM = RoutePlatform.KR
    LEAGUE_ID = "74e32628-c4c8-30e4-9835-1a35f272a62a"

    json_str = load_test_json("get_league_by_league_id.json")
    expected_response = LeagueListDTO.model_validate_json(json_str)

    route = respx.route(
        method="GET",
        host="kr.api.riotgames.com",
        path="/lol/league/v4/leagues/74e32628-c4c8-30e4-9835-1a35f272a62a",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response, headers = await client.get_league_by_league_id(ROUTE_PLATFORM, LEAGUE_ID)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_challenger_league(client: Client):
    from riot_api.types.request import RoutePlatform, RankedQueue
    from riot_api.types.dto.league_dto import LeagueListDTO

    ROUTE_PLATFORM = RoutePlatform.KR
    QUEUE = RankedQueue.RANKED_SOLO_5x5

    json_str = load_test_json("get_challenger_league.json")
    expected_response = LeagueListDTO.model_validate_json(json_str)

    route = respx.route(
        method="GET",
        host="kr.api.riotgames.com",
        path="/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response, headers = await client.get_challenger_league(ROUTE_PLATFORM, QUEUE)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_grandmaster_league(client: Client):
    from riot_api.types.request import RoutePlatform, RankedQueue
    from riot_api.types.dto.league_dto import LeagueListDTO

    ROUTE_PLATFORM = RoutePlatform.KR
    QUEUE = RankedQueue.RANKED_SOLO_5x5

    json_str = load_test_json("get_grandmaster_league.json")
    expected_response = LeagueListDTO.model_validate_json(json_str)

    route = respx.route(
        method="GET",
        host="kr.api.riotgames.com",
        path="/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response, headers = await client.get_grandmaster_league(ROUTE_PLATFORM, QUEUE)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_master_league(client: Client):
    from riot_api.types.request import RoutePlatform, RankedQueue
    from riot_api.types.dto.league_dto import LeagueListDTO

    ROUTE_PLATFORM = RoutePlatform.KR
    QUEUE = RankedQueue.RANKED_SOLO_5x5

    json_str = load_test_json("get_master_league.json")
    expected_response = LeagueListDTO.model_validate_json(json_str)

    route = respx.route(
        method="GET",
        host="kr.api.riotgames.com",
        path="/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response, headers = await client.get_master_league(ROUTE_PLATFORM, QUEUE)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response
