from src.disaster_prediction import CustomLogger

logger = CustomLogger().get_logger()
logger.info("Logging from another module")

from src.disaster_prediction.config.configuration import ConfigurationManager

config=ConfigurationManager()