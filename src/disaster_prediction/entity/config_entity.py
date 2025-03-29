from pathlib import Path
from dataclasses import dataclass

# Define a data class
@dataclass
class DataIngestionConfig:
  root_dir:Path
  zip_path:Path
  extract_path:Path
  dataset_name:str

@dataclass
class DataTransformationConfig:
  root_dir:Path
  raw_data_path:Path
  x_path:Path
  y_path:Path
  random_state:int
  split_size:float

# Define a data class
@dataclass
class ModelTrainingConfig:
  root_dir:Path
  model_path:Path
  training:dict

@dataclass
class PredictionConfig:
  model_path:Path

  