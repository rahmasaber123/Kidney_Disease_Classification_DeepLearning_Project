import os
from box import ConfigBox
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from typing import Any, List  # ✅ Added List here
from pathlib import Path
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns the content as a ConfigBox."""
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
        logger.info(f"✅ YAML file loaded successfully: {path_to_yaml}")
        return ConfigBox(content)

    except BoxValueError as e:
        logger.error(f"❌ BoxValueError while reading YAML: {e}")
        raise e
    except Exception as e:
        logger.error(f"❌ Error reading YAML file {path_to_yaml}: {e}")
        raise e



def create_directories(path_to_directories):
    """Creates directories if they don't exist."""
    if not isinstance(path_to_directories, (list, tuple)):
        path_to_directories = [path_to_directories]

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logger.info(f"📁 Directory created at: {path}")



@ensure_annotations
def save_json(path: Path, data: dict[str, Any]) -> None:
    """Saves a dictionary as a JSON file."""
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    logger.info(f"💾 JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns the content as a ConfigBox."""
    with open(path, "r") as json_file:
        content = json.load(json_file)
    logger.info(f"📄 JSON file loaded from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path) -> None:
    """Saves data to a binary file using joblib."""
    joblib.dump(data, path)
    logger.info(f"💾 Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib."""
    data = joblib.load(path)
    logger.info(f"📦 Binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """Returns the size of a file in KB."""
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~ {size_in_kb} KB"


@ensure_annotations
def encodeImageIntoBase64(image_path: Path) -> str:
    """Encodes an image file into base64 string."""
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode("utf-8")
    logger.info(f"🖼️ Image encoded to base64: {image_path}")
    return b64_string


@ensure_annotations
def decodeBase64ToImage(b64_string: str, output_path: Path) -> None:
    """Decodes a base64 string into an image file."""
    with open(output_path, "wb") as img_file:
        img_file.write(base64.b64decode(b64_string))
    logger.info(f"📸 Base64 decoded and saved to: {output_path}")
