import os
from src.disaster_prediction import CustomLogger
logger = CustomLogger().get_logger()

def create_directory(directory_path):
    try:
        # Create the directory along with any intermediate directories if they don't exist
        os.makedirs(directory_path, exist_ok=True)
        logger.info(f"Directory '{directory_path}' created successfully!")
    except Exception as e:
        logger.info(f"Error creating directory '{directory_path}': {e}")

import yaml

def read_yaml(file_path):
    """
    Reads a YAML file and returns its contents as a Python dictionary.

    :param file_path: Path to the YAML file.
    :return: Dictionary containing YAML data.
    """
    try:
        with open(file_path, "r") as file:
            data = yaml.safe_load(file)
        return data
    except FileNotFoundError:
        logger.info(f"Error: File not found at {file_path}")
        return None
    except yaml.YAMLError as e:
        logger.info(f"Error parsing YAML file: {e}")
        return None