from src.disaster_prediction.config.configuration import ConfigurationManager
from src.disaster_prediction.components.data_transformation import DataTransformation

def DataTransformationPipeline():
  config=ConfigurationManager()
  data_transformation_config=config.DataTransformationManager()
  data_transformation=DataTransformation(data_transformation_config)
  x_train, x_test, y_train, y_test=data_transformation.data_transformation()
  return x_train, x_test, y_train, y_test