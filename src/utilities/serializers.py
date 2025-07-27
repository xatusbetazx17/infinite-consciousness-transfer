"""
YAML/JSON serialization utilities

Provides functions to load and dump Python objects (dicts, lists, etc.)
as YAML and JSON files, with safe handling and optional pretty-printing.
"""
import os
import json
from typing import Any

try:
    import yaml
    _HAS_YAML = True
except ImportError:
    _HAS_YAML = False


def to_json(obj: Any, path: str, indent: int = 2) -> None:
    """
    Serialize a Python object to a JSON file.

    :param obj: Python object (e.g., dict, list)
    :param path: File path to write (will overwrite existing)
    :param indent: Indentation level for pretty-printing
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(obj, f, indent=indent)


def from_json(path: str) -> Any:
    """
    Load a Python object from a JSON file.

    :param path: File path to read
    :return: Deserialized Python object
    :raises FileNotFoundError: if the file does not exist
    :raises json.JSONDecodeError: if the file is invalid JSON
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"JSON file not found: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def to_yaml(obj: Any, path: str, default_flow_style: bool = False) -> None:
    """
    Serialize a Python object to a YAML file.

    :param obj: Python object (e.g., dict, list)
    :param path: File path to write (will overwrite existing)
    :param default_flow_style: if True, more compact YAML
    :raises ImportError: if PyYAML is not installed
    """
    if not _HAS_YAML:
        raise ImportError("PyYAML is not installed. Cannot serialize to YAML.")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        yaml.safe_dump(obj, f, default_flow_style=default_flow_style)


def from_yaml(path: str) -> Any:
    """
    Load a Python object from a YAML file.

    :param path: File path to read
    :return: Deserialized Python object
    :raises ImportError: if PyYAML is not installed
    :raises FileNotFoundError: if the file does not exist
    :raises yaml.YAMLError: if the file contains invalid YAML
    """
    if not _HAS_YAML:
        raise ImportError("PyYAML is not installed. Cannot load YAML.")
    if not os.path.isfile(path):
        raise FileNotFoundError(f"YAML file not found: {path}")
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


# Basic test cases
if __name__ == '__main__':
    print("=== Running serializers.py Tests ===")
    sample = {'a': 1, 'b': [2, 3], 'c': {'nested': True}}
    # JSON round-trip
    json_path = 'test_outputs/sample.json'
    to_json(sample, json_path)
    loaded_json = from_json(json_path)
    assert loaded_json == sample, "JSON round-trip failed"
    print("JSON serialization tests passed.")
    # YAML round-trip (if available)
    if _HAS_YAML:
        yaml_path = 'test_outputs/sample.yaml'
        to_yaml(sample, yaml_path)
        loaded_yaml = from_yaml(yaml_path)
        assert loaded_yaml == sample, "YAML round-trip failed"
        print("YAML serialization tests passed.")
    else:
        print("PyYAML not installed; skipping YAML tests.")
