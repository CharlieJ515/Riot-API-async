import asyncio
import os

from dotenv import load_dotenv

from riot_api import Client
from riot_api.types.request import RouteRegion
from riot_api.types.dto import AccountDTO, AccountRegionDTO


async def main():
    load_dotenv()

    api_key = os.environ.get("RIOT_API_KEY")
    if not api_key:
        raise ValueError("Please set the RIOT_API_KEY environment variable.")

    client = Client(api_key)

    # Example 1: Get account by Riot ID
    account, headers = await client.get_account_by_riot_id(
        route=RouteRegion.ASIA,
        game_name="summer",
        tag_line="pado",
    )
    print(f"Account by Riot ID: {account.model_dump()}")

    # Example 2: Get account by PUUID
    account, headers = await client.get_account_by_puuid(
        route=RouteRegion.ASIA,
        puuid="l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w",
    )
    print(f"Account by PUUID: {account.model_dump()}")

    # Example 3: Get account region
    account_region, headers = await client.get_account_region(
        route=RouteRegion.ASIA,
        game="lol",
        puuid="l51rA9uBuXO1Zokld038OVu0aRhDKA2NcE5J5Ng2LmMxzZ2gJArIa5v_UaiEmHSDdSyKsbiiawWX_w",
    )
    print(f"Account region: {account_region.model_dump()}")


if __name__ == "__main__":
    asyncio.run(main())
