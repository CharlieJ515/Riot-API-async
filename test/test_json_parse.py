import json
import pprint
import numbers

import pytest
from conftest import load_test_json
from deepdiff import DeepDiff

from riot_api.types.dto import (
    AccountDTO,
    AccountRegionDTO,
    LeagueListDTO,
    LeagueEntryListDTO,
    MatchDTO,
    TimelineDTO,
    MatchIdListDTO,
)
from riot_api.utils import normalize_string


def remove_trivial_added_none_fields(diff):
    """
    Remove 'dictionary_item_added' fields with value 'None' (optional fields)
    """
    added = diff.get("dictionary_item_added", {})
    keys_to_remove = []

    for path, value in added.items():
        if value is None:
            keys_to_remove.append(path)

    for key in keys_to_remove:
        del added[key]

    if not added:
        diff.pop("dictionary_item_added", None)


def remove_trivial_zero_numeric_type_diffs(diff):
    """
    Remove 'type_changes' where old and new are numeric, ends in zero, but have different types (int vs float).
    E.g., 3 and 3.0
    """
    type_changes = diff.get("type_changes", {})
    keys_to_remove = []

    for path, change in type_changes.items():
        old_value, new_value = change.get("old_value"), change.get("new_value")
        # Check both are numeric
        if isinstance(old_value, numbers.Number) and isinstance(
            new_value, numbers.Number
        ):
            if old_value == new_value:
                keys_to_remove.append(path)

    for key in keys_to_remove:
        del type_changes[key]

    if not type_changes:
        diff.pop("type_changes", None)


def remove_trivial_normalized_string_diffs(diff):
    """
    Remove 'values_changed' where old_value is a string and
    normalizing it makes it equal to new_value.
    """
    values_changed = diff.get("values_changed", {})
    keys_to_remove = []

    for path, change in values_changed.items():
        old_value = change.get("old_value")
        new_value = change.get("new_value")
        if isinstance(old_value, str) and isinstance(new_value, str):
            if normalize_string(old_value) == new_value:
                keys_to_remove.append(path)

    for key in keys_to_remove:
        del values_changed[key]

    if not values_changed:
        diff.pop("values_changed", None)


@pytest.mark.parametrize(
    "filename, dto_class",
    [
        ("get_account_by_puuid.json", AccountDTO),
        ("get_account_region.json", AccountRegionDTO),
        ("get_match_by_match_id.json", MatchDTO),
        ("get_match_timeline.json", TimelineDTO),
    ],
)
def test_parse_dto_matches_json_dict(filename, dto_class):
    json_str = load_test_json(filename)

    expected_dict = json.loads(json_str)

    model = dto_class.model_validate_json(json_str)
    parsed_dict = model.model_dump(by_alias=True)

    diff = DeepDiff(expected_dict, parsed_dict, verbose_level=2)
    remove_trivial_added_none_fields(diff)
    remove_trivial_zero_numeric_type_diffs(diff)
    remove_trivial_normalized_string_diffs(diff)

    if diff:
        formatted_diff = pprint.pformat(diff, width=120)
        raise AssertionError(f"JSON mismatch:\n{formatted_diff}")
