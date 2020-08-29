import json
import typing as t

import typeguard
from typeguard import check_type
REQUIRED_FIELDS = {"timestamp", "buffer", "cursor_position", "visual_selection"}

Position = t.Tuple[int, int] # (line_number, char_number)
FIELD_TYPES = {
	"timestamp": float,
	"buffer": str,
	"cursor_position": Position,
	"visual_selection": t.List[Position]
}

def _check_type(object, type):
	try:
		check_type('_', object, type)
		return True
	except TypeError:
		return False

def is_valid_structure(content: t.Any) -> bool:

	if not isinstance(content, list):
		return False
	for entry in content:
		if set(entry.keys()) != REQUIRED_FIELDS:
			return False
	return True

def are_entry_types_valid(entry: t.Dict[str, t.Any]) -> bool:
	assert set(entry.keys()) == REQUIRED_FIELDS
	for field_name, field_type in FIELD_TYPES.items():
		# print(typeguard.check_type(field_name, entry[field_name], field_type))
		if not _check_type(entry[field_name], field_type):
			return False
	return True


def are_content_types_valid(content: t.List[t.Dict[str, t.Any]]) -> bool:
	for entry in content:
		if not are_entry_types_valid(entry):
			return False
	return True

def is_valid_content(content: t.Any) -> bool:
	if not is_valid_structure(content):
		return False
	if not are_content_types_valid(content):
		return False
	return True

def is_valid(f: t.TextIO) -> bool:
	assert (not f.closed)
	content = json.load(f)
	return is_valid_content(content=content)

def is_valid_file(file_name: str) -> bool:
	with open(file_name, 'r') as f:
		return is_valid(f)

def is_valid_json_str(json_str: str) -> bool:
	return is_valid_content(json.loads(json_str))