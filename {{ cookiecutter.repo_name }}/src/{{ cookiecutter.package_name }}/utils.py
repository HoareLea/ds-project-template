import yaml
import json
import os

hl_colors = [
    '#343334',
    '#d02e6f',
    '#e3ed64',
    '#b5d1c0',
    '#7aaabe',
    '#9b8dc6',
    '#5d5c5d',
    '#f1f6b1',
    '#cbdfd3',
    '#aac9d3',
    '#c1a5d7',
    '#858485'
]

def load_yaml_to_dict(file_path: str) -> dict:
    """
    Load a YAML file into a dictionary.

    Args:
    data (dict): The dictionary to save.
    file_path (str): The path to the file where the YAML data will be saved.

    Returns:
    None
    """
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
    
def save_dict_to_yaml(data: dict, file_path: str) -> None:
    """
    Save a dictionary to a YAML file.

    Args:
    data (dict): The dictionary to save.
    file_path (str): The path to the file where the YAML data will be saved.

    Returns:
    None
    """
    with open(file_path, 'w') as file:
        yaml.dump(data, file)

def load_json_to_dict(file_path: str) -> dict:
    """
    Load a JSON file into a dictionary.

    Args:
    data (dict): The dictionary to save.
    file_path (str): The path to the file where the JSON data will be saved.

    Returns:
    None
    """
    with open(file_path, 'r') as file:
        return json.load(file)
    
def save_dict_to_json(data: dict, file_path: str) -> None:
    """
    Save a dictionary to a JSON file.

    Args:
    data (dict): The dictionary to save.
    file_path (str): The path to the file where the JSON data will be saved.

    Returns:
    None
    """
    with open(file_path, 'w') as file:
        json.dump(data, file)

def ensure_directory_exists(dir_path: str) -> None:
    """
    Ensure that a directory exists; if it does not, create it.

    Args:
    dir_path (str): The path to the directory.

    Returns:
    None
    """
    os.makedirs(dir_path, exist_ok=True)

def list_files(directory: str, extension: list[str] = None) -> list[str]:
    """
    List files in a directory.

    Args:
    directory (str): The directory to list files from.
    extension ([str]): Optional - A list of file extensions to filter by.

    Returns:
    List[str]: A list of file paths.
    """
    if extension is None:
        return [os.path.join(directory, file) for file in os.listdir(directory)]
    else:
        return [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith(extension)]
