import pandas as pd
import os
from numpy import divide, argmax
import keras, keras_nlp
from keras.losses import SparseCategoricalCrossentropy, BinaryCrossentropy
from keras.optimizers import Adam
from src.disaster_prediction.entity.config_entity import ModelTrainingConfig

class Vocabulary(set):
    """Vocabulary, a set with unique words from our text features."""

    def extend(self, texts):
        """Add all words from a text"""
        for t in texts:
            self.update(re.findall(r"[\w']+|[.,!?;]", t))

    def export(self):
        """Cast set as a list"""
        self.update(["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
        return list(self)

class ModelTraining:
  def __init__(self,config:ModelTrainingConfig):
    self.config=config
    self.params=config.training

  def get_model(self, vocab=[]):
    # Tokenizer
    tokenizer = keras_nlp.models.BertTokenizer(vocabulary=vocab)
    # Preprocess
    preprocessor = keras_nlp.models.BertPreprocessor(tokenizer=tokenizer, sequence_length=self.params["sequence_length"])
    # Backbone
    backbone = keras_nlp.models.BertBackbone(
        vocabulary_size=self.params["vocabulary_size"],
        num_layers=self.params["num_layers"],
        num_heads=self.params["num_heads"],
        hidden_dim=self.params["hidden_dim"],
        intermediate_dim=self.params["intermediate_dim"],
        max_sequence_length=self.params["max_sequence_length"]
    )
    # Classifier
    classifier = keras_nlp.models.BertClassifier(
        backbone=backbone,
        preprocessor=preprocessor,
        num_classes=self.params["labels_count"],
        activation=self.params["activation"]
    )
    # Compile classifier
    classifier.compile(
        loss=SparseCategoricalCrossentropy(from_logits=False),
        optimizer=Adam(5e-5),
        metrics=[self.params["metric1"],self.params["metric2"],self.params["metric3"]]
    )
    return classifier

  def train_model(self,x_train,x_test,y_train):

    vocab = Vocabulary()

    for v in (x_train, x_test): vocab.extend(v)

    # Prepare vocabulary
    vocab = vocab.export()

    # Get the model
    m = self.get_model(vocab=vocab)

    # Train the model
    history = m.fit(x=x_train, y=y_train, batch_size=self.params["batch_size"], epochs=self.params["epochs"], shuffle=self.params["shuffle"])
    keras.saving.save_model(m, self.config.model_path)