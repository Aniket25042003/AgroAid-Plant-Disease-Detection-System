# -*- coding: utf-8 -*-
"""plant diseases detection model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EDvOCE0R6HET2AswuNlbNHzvpuWnd6pF

Install Kaggle
"""

!pip install kaggle

"""Upload your Kaggle.json file to google colab"""

from google.colab import files
files.upload()

"""Move and Set Permissions for kaggle.json"""

!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

"""Download the dataset from kaggle"""

!kaggle datasets download -d vipoooool/new-plant-diseases-dataset

"""Unzip the dataset"""

!unzip new-plant-diseases-dataset.zip

"""Import the required libraries"""

import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""Training Image Preprocessing"""

training_set = tf.keras.utils.image_dataset_from_directory(
    '/content/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/train',
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=32,
    image_size=(128, 128),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    data_format=None,
    verbose=True,
)

"""Validation Image Preprocessing"""

validation_set = tf.keras.utils.image_dataset_from_directory(
    '/content/New Plant Diseases Dataset(Augmented)/New Plant Diseases Dataset(Augmented)/valid',
    labels="inferred",
    label_mode="categorical",
    class_names=None,
    color_mode="rgb",
    batch_size=32,
    image_size=(128, 128),
    shuffle=True,
    seed=None,
    validation_split=None,
    subset=None,
    interpolation="bilinear",
    follow_links=False,
    crop_to_aspect_ratio=False,
    pad_to_aspect_ratio=False,
    data_format=None,
    verbose=True,
)

"""Model Building"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

model = Sequential()

"""Adding Layers"""

model.add(Conv2D(filters=32, kernel_size=3, activation='relu', input_shape=(128, 128, 3), padding='same'))
model.add(Conv2D(filters=32, kernel_size=3, activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(filters=64, kernel_size=3, activation='relu', input_shape=(128, 128, 3), padding='same'))
model.add(Conv2D(filters=64, kernel_size=3, activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(filters=128, kernel_size=3, activation='relu', input_shape=(128, 128, 3), padding='same'))
model.add(Conv2D(filters=128, kernel_size=3, activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(filters=256, kernel_size=3, activation='relu', input_shape=(128, 128, 3), padding='same'))
model.add(Conv2D(filters=256, kernel_size=3, activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Conv2D(filters=512, kernel_size=3, activation='relu', input_shape=(128, 128, 3), padding='same'))
model.add(Conv2D(filters=512, kernel_size=3, activation='relu'))
model.add(MaxPooling2D((2, 2)))

model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(units=2048, activation='relu'))
model.add(Dense(units=38, activation='softmax'))

"""Model Compilation"""

model.compile(optimizer=tf.keras.optimizers.Adam(
    learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

"""Model Training"""

training_history = model.fit(training_set, validation_data=validation_set, epochs=10)

"""Model Evaluation

Model Evaluation on Training Set
"""

training_loss, training_accuracy = model.evaluate(training_set)
print(f"Training Loss: {training_loss}")
print(f"Training Accuracy: {training_accuracy}")

"""Model Evaluation on Validation Set"""

validation_loss, validation_accuracy = model.evaluate(validation_set)
print(f"Validation Loss: {validation_loss}")
print(f"Validation Accuracy: {validation_accuracy}")

"""Saving Model"""

model.save('mydrive/plant diseases detection model/plant_disease_model.h5')

model.save('mydrive/plant diseases detection model/plant_disease_model.keras')