from src.disaster_prediction.utils.common import read_yaml, create_directory
from src.disaster_prediction.entity.config_entity import DataIngestionConfig, DataTransformationConfig, ModelTrainingConfig, PredictionConfig

class ConfigurationManager:
  def __init__(self):
    #read yaml files here
    self.config=read_yaml("config/config.yaml")
    self.param=read_yaml("params.yaml")
    self.root_dir=self.config["root"]
    create_directory(self.root_dir)

  def DataIngestionManager(self)->DataIngestionConfig:
    config=self.config["data_ingestion"]
    create_directory(config["root_dir"])
    data_ingestion_config=DataIngestionConfig(
      root_dir=config["root_dir"],
      zip_path=config["zip_path"],
      extract_path=config["extract_path"],
      dataset_name=config["dataset_name"]
    )
    return data_ingestion_config

  def DataTransformationManager(self)->DataTransformationConfig:
    config=self.config["data_transformation"]
    param=self.param["data_transformation"]
    create_directory(config["root_dir"])
    data_transformation_config=DataTransformationConfig(
        root_dir=config["root_dir"],
        raw_data_path=config["raw_data_path"],
        x_path=config["x_path"],
        y_path=config["y_path"],
        random_state=param["random_state"],
        split_size=param["split_size"]
    )
    return data_transformation_config

  def ModelTrainingManager(self)->ModelTrainingConfig:
    config=self.config["model_training"]
    param=self.param["model_training"]
    create_directory(config["root_dir"])
    model_training_config=ModelTrainingConfig(
        root_dir=config["root_dir"],
        model_path=config["model_path"],
        training=param
    )
    return model_training_config

  def PredictionManager(self)->PredictionConfig:
    config=self.config["prediction"]
    prediction_config=PredictionConfig(
        model_path=config["model_path"]
    )
    return prediction_config