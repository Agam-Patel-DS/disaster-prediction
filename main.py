from src.disaster_prediction import CustomLogger

logger = CustomLogger().get_logger()
logger.info("Logging from another module")