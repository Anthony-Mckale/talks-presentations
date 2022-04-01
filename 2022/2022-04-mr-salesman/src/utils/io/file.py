"""IO helpers
"""
import json
import os
import re
from pathlib import Path

def sane(key):
    """sanitise keys to be Alpha-numerical"""
    if not key:
        return ""
    return re.sub("[^a-zA-Z0-9_-]", "_", key)


def normalise_file_paths(file_paths: list) -> Path:
    """Clean up user inputted filename path makes all"""
    new_file_paths = list(map(normalise_linux_file_path, file_paths))
    return new_file_paths


def remove_non_folders(file_paths: list, default: list, subject: str) -> list:
    """Removes non folders and non existent entries"""
    cleaned = []
    for file_path in file_paths:
        local_folder = Path.cwd() / file_path
        if not os.path.exists(local_folder):
            continue
        if not os.path.isdir(local_folder):
            print(
                f"{subject}: Removing non folder '{local_folder}' from list '{file_paths}'"
            )
            continue
        cleaned.append(file_path)
    if len(cleaned) == 0:
        print(f"{subject}: No valid paths left, defaulting to '{default}'")
        return default
    return cleaned


def is_windows_os() -> bool:
    """Is running on a windows machine
    see https://docs.python.org/3/library/os.html
    """
    os_name = os.name
    return os_name == "nt"


def normalise_linux_file_path(file_path: str) -> Path:
    """Clean up user inputted filename path makes all back slashes forward slashes"""
    file_path = re.sub("\\\\", "/", file_path)
    return file_path


def normalise_windows_regex_file_path(file_path: str) -> Path:
    """Clean up user inputted filename path makes all forward 4 escaped back slashes slashes"""
    file_path = re.sub("/", "\\\\\\\\", file_path)
    return file_path


def get_absolute_filename(user_inputted_filename: str) -> Path:
    """Clean up user inputted filename path, wraps os.path.abspath, returns Path object"""
    filename_location = Path(os.path.abspath(user_inputted_filename))
    return filename_location


def load_text(file_path: str) -> str:
    """
    Load text file

    :raises Error
    """
    try:
        with open(file_path, "r", encoding="utf-8") as text_file:
            text_str = text_file.read()
        text_file.close()
        return text_str

    except PermissionError as not_permitted_err:
        raise Exception(
            f"Eze cannot access '{not_permitted_err.filename}', Permission was denied"
        )
    except FileNotFoundError as not_found_err:
        raise Exception(
            f"Eze cannot access '{not_found_err.filename}', File could not be found"
        )


def parse_json(json_str: str):
    """
    Load json string and convert to dict

    :raises Exception
    """
    try:
        return json.loads(json_str)
    except json.decoder.JSONDecodeError as error:
        raise Exception(
            f"Unable to parse JSON fragment, message: '{error.msg}' (line {error.lineno})"
        )


def load_json(file_path: str):
    """
    Load json file and convert to dict

    :raises Exception
    """
    json_str = load_text(file_path)
    if not json_str:
        return []
    try:
        return json.loads(json_str)
    except json.decoder.JSONDecodeError as error:
        raise Exception(
            f"Unable to parse JSON file '{file_path}', message: '{error.msg}' (line {error.lineno})"
        )
