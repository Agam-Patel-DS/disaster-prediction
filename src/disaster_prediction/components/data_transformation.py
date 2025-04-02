import pandas as pd
import os
from src.disaster_pre

class DataTransformation:
  def __init__(self,config:DataTransformationConfig):
    self.config=config

  def text_cleaning(self,text):
    """Clean text"""
    # Lower text
    text = text.lower()
    # Clean from urls
    urls = re.compile(r'https?://\S+|www\.\S+').findall(text)
    for url in urls: text = text.replace(url, '')
    # Clean from hashtags and mentions marks
    for t in ('@', '#'): text = text.replace(t, '')
    return text

  def data_processing(self,data):
      """Process data"""
      d = data[['text', 'target']]
      # Preprocess dataset
      x = [self.text_cleaning(v) for v in d['text'].to_list()]
      y = d['target'].to_list()
      return x, y

  def data_transformation(self):
      """Get dataset by split name (train/validation/test)"""
      # Load data
      df = pd.read_csv(self.config.raw_data_path)
      # Process data
      x, y = self.data_processing(df)
      pd.DataFrame(y).to_csv(self.config.y_path)
      pd.DataFrame(x).to_csv(self.config.x_path)
      # Split dataset into training and test set
      x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=self.config.split_size, random_state=self.config.random_state)
      return x_train, x_test, y_train, y_test