import json
import re

# Path to your champion.json file
champion_json_path = "datadragon/champion.json"

with open(champion_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

champions = data["data"]

print("from enum import IntEnum, StrEnum\n")

# ChampionId enum
print("class ChampionId(IntEnum):")
for champ in champions.values():
    # Remove non-alphabet characters from id and convert to uppercase
    member_name = re.sub(r"[^A-Za-z]", "", champ["id"]).upper()
    champ_id = champ["key"]
    print(f"    {member_name} = {champ_id}")
print()

# ChampionName enum
print("class ChampionName(StrEnum):")
for champ in champions.values():
    member_name = re.sub(r"[^A-Za-z]", "", champ["id"]).upper()
    champ_name = re.sub(r"[^A-Za-z]", "", champ["name"]).lower()
    print(f'    {member_name} = "{champ_name}"')
