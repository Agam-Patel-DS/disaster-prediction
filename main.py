from src.disaster_prediction import CustomLogger
from src.disaster_prediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline

logger = CustomLogger().get_logger()
logger.info("Logging from another module")

from src.disaster_prediction.config.configuration import ConfigurationManager


logger.info("<<<<<< Data Ingestion Started >>>>>>")
DataIngestionPipeline()
logger.info("<<<<<< Data Ingestion Done >>>>>>>")