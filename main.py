from src.disaster_prediction import CustomLogger
from src.disaster_prediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.disaster_prediction.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.disaster_prediction.pipeline.model_training_pipeline import ModelTrainingPipeline


logger = CustomLogger().get_logger()
logger.info("Logging from another module")

from src.disaster_prediction.config.configuration import ConfigurationManager


logger.info("<<<<<< Data Ingestion Started >>>>>>")
DataIngestionPipeline()
logger.info("<<<<<< Data Ingestion Done >>>>>>>")


logger.info("<<<<<< Data Transformation Started >>>>>>")
x_train, x_test, y_train, y_test=DataTransformationPipeline()
logger.info("<<<<<< Data Transformation Done >>>>>>>")


logger.info("<<<<<< Model Training Started >>>>>>")
ModelTrainingPipeline(x_train, x_test, y_train)
logger.info("<<<<<< Model Training Done >>>>>>>")