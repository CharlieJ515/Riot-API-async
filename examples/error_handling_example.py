import asyncio
import os

from dotenv import load_dotenv
from riot_api import Client
from riot_api.types.request import RouteRegion
from riot_api.exceptions import RiotAPIError, UnauthorizedError, RateLimitError


async def main():
    api_key = "Invalid Api Key"

    client = Client(api_key)

    try:
        # Use a clearly invalid Riot ID to trigger an error
        game_name = "nonexistentuser"
        tag_line = "NA1"

        response, headers = await client.get_account_by_riot_id(
            route=RouteRegion.ASIA,
            game_name=game_name,
            tag_line=tag_line,
        )
        print(f"Account found: {response.gameName}#{response.tagLine}")

    except UnauthorizedError:
        print("Unauthorized – your API key may be missing or expired.")
    except RateLimitError as e:
        print(f"Rate limit exceeded. Retry after {e.retry_after} seconds.")
    except RiotAPIError as e:
        print(f"Riot API returned an error: {e}")
    except Exception as e:
        print(f"Unhandled exception: {e}")
    finally:
        await client.close_session()


if __name__ == "__main__":
    asyncio.run(main())
