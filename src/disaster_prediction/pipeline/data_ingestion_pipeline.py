from src.disaster_prediction.config.configuration import ConfigurationManager
from src.disaster_prediction.components.data_ingestion import DataIngestion

def DataIngestionPipeline():
  config=ConfigurationManager()
  data_ingestion_config=config.DataIngestionManager()
  data_ingestion=DataIngestion(data_ingestion_config)
  data_ingestion.download_data()