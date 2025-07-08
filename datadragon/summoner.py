import json
import re

# Path to your summoner.json file (adjust if needed)
summoner_json_path = "datadragon/summoner.json"

with open(summoner_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

spells = data["data"]

print("from enum import IntEnum\n")
print("class SummonerSpell(IntEnum):")

for spell in spells.values():
    spell_id = spell["key"]
    raw_name = spell["name"]

    # Remove all non-alphabet characters and convert to uppercase
    cleaned_name = re.sub(r"[^A-Za-z]", "", raw_name).upper()

    # Always append the spell ID for clarity and uniqueness
    member_name = f"{cleaned_name}_{spell_id}"

    print(f"    {member_name} = {spell_id}")
