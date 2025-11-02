import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from typing import Any
from pathlib import Path
import base64


ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a yaml file and returns the content

    Args:
        path_to_yaml (Path): Path to the yaml file

    Returns:
        Any: Content of the yaml file
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
        logger.info(f"YAML file: {path_to_yaml} loaded successfully")
        return ConfigBox(content)
    
    except BoxValueError as e:
        logger.error(f"Error reading the YAML file: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error reading the YAML file: {e}")
        raise e
@ensure_annotations
def create_directories(path_to_directories: list[Path]) -> None:
    """Creates a list of directories

    Args:
        path_to_directories (list[Path]): List of directory paths
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"Directory created at: {path}")
@ensure_annotations
def save_json(path: Path, data: dict[str, Any]) -> None:
    """Saves a dictionary to a json file

    Args:
        path (Path): Path to the json file
        data (dict[str, Any]): Data to be saved
    """
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"JSON file saved at: {path}")
@ensure_annotations
def load_json(path: Path) -> dict[str, Any]:
    """Loads a json file and returns the content

    Args:
        path (Path): Path to the json file

    Returns:
        dict[str, Any]: Content of the json file
    """
    with open(path, "r") as json_file:
        content = json.load(json_file)
    logger.info(f"JSON file loaded from: {path}")
    return  ConfigBox(content )
@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Saves data to a binary file using joblib

    Args:
        data (Any): Data to be saved
        path (Path): Path to the binary file
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations

def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib

    Args:
        path (Path): Path to the binary file    
    Returns:
        Any: Loaded data
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data 
@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB

    Args:
        path (Path): Path to the file

    Returns:
        str: Size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"
@ensure_annotations
def encodeImageIntoBase64(image_path: Path) -> str:
    """Encodes an image to base64 format

    Args:
        image_path (Path): Path to the image file

    Returns:
        str: Base64 encoded string of the image
    """
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode("utf-8")
    logger.info(f"Image at {image_path} encoded to base64")
    return b64_string
@ensure_annotations
def decodeBase64ToImage(b64_string: str, output_path: Path) -> None:
    """Decodes a base64 string and saves it as an image file

    Args:
        b64_string (str): Base64 encoded string of the image
        output_path (Path): Path to save the decoded image file
    """
    with open(output_path, "wb") as img_file:
        img_file.write(base64.b64decode(b64_string))
    logger.info(f"Base64 string decoded and saved to {output_path}")