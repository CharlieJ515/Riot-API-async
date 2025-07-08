import json
import re

# Path to your items.json file (adjust as needed)
items_json_path = "datadragon/item.json"

with open(items_json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

items = data["data"]

print("from enum import IntEnum\n")
print("class ItemId(IntEnum):")
print("    NONE_0 = 0")  # Add NONE at the top of the enum

for item_id, item_data in items.items():
    raw_name = item_data["name"]

    # Skip items with any markup tags like <RARITYLEGENDARY> etc.
    if re.search(r"<[^>]+>", raw_name):
        continue

    # Remove all non-alphabet characters and convert to uppercase
    cleaned_name = re.sub(r"[^A-Za-z]", "", raw_name).upper()

    if not cleaned_name:
        continue

    # Always append item ID, even without duplicates
    member_name = f"{cleaned_name}_{item_id}"

    print(f"    {member_name} = {item_id}")
