from src.disaster_prediction.entity.config_entity import DataIngestionConfig
from src.disaster_prediction.utils.common import create_directory

import subprocess
import zipfile
import os
import shutil
import os
import zipfile
import shutil
import subprocess

def create_directory(dir_path):
    """Creates a directory if it doesn't exist."""
    os.makedirs(dir_path, exist_ok=True)

def download_and_unzip_kaggle_dataset(dataset_name, zip_path, extract_path):
    """Downloads and extracts a dataset from Kaggle."""
    create_directory(os.path.dirname(zip_path))
    create_directory(os.path.dirname(extract_path))

    # Download the dataset from Kaggle (without specifying file name)
    subprocess.run(['kaggle', 'datasets', 'download', dataset_name, '-p', os.path.dirname(zip_path)], check=True)

    # Find the downloaded ZIP file (Kaggle names it as dataset_name.zip)
    zip_file = os.path.join(os.path.dirname(zip_path), dataset_name.split('/')[-1] + '.zip')
    
    if not os.path.exists(zip_file):
        raise FileNotFoundError(f"Expected ZIP file not found: {zip_file}")

    # Move and rename the ZIP file
    shutil.move(zip_file, zip_path)

    # Extract all files
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(os.path.dirname(extract_path))

    print(f"Dataset downloaded and extracted to {os.path.dirname(extract_path)}")

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_data(self):
        download_and_unzip_kaggle_dataset(self.config.dataset_name, self.config.zip_path, self.config.extract_path)
