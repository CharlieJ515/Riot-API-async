import re


def normalize_string(s: str) -> str:
    """remove non-alphabetic characters then lowercase"""
    return re.sub(r"[^a-zA-Z]", "", s).lower()
