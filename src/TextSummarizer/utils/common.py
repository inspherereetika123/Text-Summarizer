import os
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from typeguard import typechecked
from box import ConfigBox
from pathlib import Path
from typing import Any, List


@typechecked
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns its content as a ConfigBox object."""
    try:
        if not path_to_yaml.exists():
            logger.error(f"YAML file not found: {path_to_yaml}")
            raise FileNotFoundError(f"No such file: {path_to_yaml}")
 
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty")

            logger.info(f"YAML file '{path_to_yaml}' loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("Invalid Box structure in YAML file")
    except Exception as e:
        logger.exception(f"Error reading YAML file: {path_to_yaml}")
        raise e


@typechecked
def create_directories(path_to_directories: list, verbose: bool = True):
    """
    Create a list of directories if they don’t already exist.
    Works even if you pass strings instead of Path objects.
    """
    for path in path_to_directories:
        path = Path(path)  # ✅ Convert string -> Path safely
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")



@typechecked
def get_size(path: Path) -> str:
    """Get size of a file in KB."""
    if not os.path.exists(path):
        logger.warning(f"File not found: {path}")
        return "~ 0 KB"

    size_in_kb = round(os.path.getsize(path) / 1024)
    logger.info(f"Size of {path}: {size_in_kb} KB")
    return f"~ {size_in_kb} KB"
