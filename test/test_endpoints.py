import os

import pytest
import pytest_asyncio
from conftest import load_test_json
import httpx
import respx

from riot_api.client import Client
from riot_api.types.request import (
    RoutePlatform,
    RouteRegion,
    RateLimit,
)
from riot_api.types.dto import (
    AccountDTO,
    AccountRegionDTO,
    MatchIdListDTO,
    MatchDTO,
    TimelineDTO,
    LeagueEntryListDTO,
    LeagueListDTO,
)

PUUID = "l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w"
GAME_NAME = "summer"
TAG_LINE = "pado"
MATCH_ID = "KR_7692293629"
ROUTE_REGION = RouteRegion.ASIA
ROUTE_PLATFORM = RoutePlatform.KR


@pytest_asyncio.fixture
async def client():
    api_key = os.environ.get("RIOT_API_KEY", "")
    rate_limit = RateLimit(max_rate=100, time_period=120)
    client = Client(api_key=api_key, rate_limit=rate_limit)
    yield client

    await client.close()


@pytest.mark.asyncio
@respx.mock
async def test_get_account_by_riot_id(client: Client):
    json_str = load_test_json("get_account_by_riot_id.json")
    expected_response = AccountDTO.model_validate_json(json_str)

    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/riot/account/v1/accounts/by-riot-id/summer/pado",
    ).mock(return_value=httpx.Response(200, content=json_str))

    response = await client.get_account_by_riot_id(ROUTE_REGION, GAME_NAME, TAG_LINE)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_account_by_puuid(client: Client):
    json_str = load_test_json("get_account_by_puuid.json")
    expected_response = AccountDTO.model_validate_json(json_str)
    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/riot/account/v1/accounts/by-puuid/l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response = await client.get_account_by_puuid(ROUTE_REGION, PUUID)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_account_region(client: Client):
    json_str = load_test_json("get_account_region.json")
    expected_response = AccountRegionDTO.model_validate_json(json_str)
    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/riot/account/v1/region/by-game/lol/by-puuid/l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response = await client.get_account_region(ROUTE_REGION, "lol", PUUID)
    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_match_by_match_id(client: Client):
    json_str = load_test_json("get_match_by_match_id.json")
    expected_response = MatchDTO.model_validate_json(json_str)
    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/lol/match/v5/matches/KR_7692293629",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response = await client.get_match_by_match_id(ROUTE_REGION, MATCH_ID)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_match_ids_by_puuid(client: Client):
    json_str = load_test_json("get_match_ids_by_puuid.json")
    expected_response = MatchIdListDTO.model_validate_json(json_str)
    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/lol/match/v5/matches/by-puuid/l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w/ids",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response = await client.get_match_ids_by_puuid(ROUTE_REGION, PUUID)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response


@pytest.mark.asyncio
@respx.mock
async def test_get_match_timeline(client: Client):
    json_str = load_test_json("get_match_timeline.json")
    expected_response = TimelineDTO.model_validate_json(json_str)
    route = respx.route(
        method="GET",
        host="asia.api.riotgames.com",
        path="/lol/match/v5/matches/KR_7692293629/timeline",
    ).mock(return_value=httpx.Response(200, content=json_str))
    response = await client.get_match_timeline(ROUTE_REGION, MATCH_ID)

    assert route.called
    assert route.call_count == 1
    assert isinstance(response, type(expected_response))
    assert response == expected_response
