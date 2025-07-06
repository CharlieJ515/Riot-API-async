from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


def load_test_json(file_name: str) -> str:
    file_path = Path(__file__).parent / "responses" / file_name
    return file_path.read_text(encoding="utf-8")
