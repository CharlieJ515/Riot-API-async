"""
Riot-API-async
"""

__author__ = "Charlie.Jang"
__version__ = "0.0.1"

from riot_api.client import Client
from riot_api.rate_limit_client import RateLimitClient


__all__ = ["Client", "RateLimitClient"]
