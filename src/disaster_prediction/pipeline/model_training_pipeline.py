from src.disaster_prediction.config.configuration import ConfigurationManager
from src.disaster_prediction.components.model_training import ModelTraining

def ModelTrainingPipeline():
  config=ConfigurationManager()
  model_training_config=config.ModelTrainingManager()
  model_training=ModelTraining(model_training_config)
  model_training.train_model(x_train, x_test, y_train)


