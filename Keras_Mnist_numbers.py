# -*- coding: utf-8 -*-
"""
Testing out keras neural networks for identifying MNIST handwritten letters
Code is from the following udemy course:
    https://www.udemy.com/course/python-for-computer-vision-with-opencv-and-deep-learning/

@author: Kalkberg
"""

# Import libraries

from keras.datasets import mnist
from keras.utils.np_utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten
# import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report

# Load data
(x_train, y_train), (x_test, y_test) = mnist.load_data()

## Pre-process data

# Set y values to one hot categories rather than 0-9
y_cat_test = to_categorical(y_test, 10)
y_cat_train = to_categorical(y_train, 10)

# Normalize x data so range of each pixel is 0-1 not 0-255
x_train = x_train/255
x_test = x_test/255

# Reshape data to give another dimension (channels) for future use

x_train = x_train.reshape(np.shape(x_train)[0],
                          np.shape(x_train)[1],
                          np.shape(x_train)[2],
                          1)

x_test = x_test.reshape(np.shape(x_test)[0],
                        np.shape(x_test)[1],
                        np.shape(x_test)[2],
                        1)

## Set up the model
model = Sequential()

# CONVOLUTIONAL LAYER
model.add(Conv2D(filters=32, kernel_size=(4,4),input_shape=(28, 28, 1), activation='relu',))

# POOLING LAYER
model.add(MaxPool2D(pool_size=(2, 2)))

# FLATTEN IMAGES FROM 28 by 28 to 764 BEFORE FINAL LAYER
model.add(Flatten())

# 128 NEURONS IN DENSE HIDDEN LAYER (YOU CAN CHANGE THIS NUMBER OF NEURONS)
model.add(Dense(64, activation='softplus'))



# LAST LAYER IS THE CLASSIFIER, THUS 10 POSSIBLE CLASSES
model.add(Dense(10, activation='softmax'))


model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
# print model summary
model.summary()

## Train model
model.fit(x_train,y_cat_train,epochs=2)

## Evaluate the model
model.metrics_names
model.evaluate(x_test,y_cat_test)
predictions = model.predict_classes(x_test)
print(classification_report(y_test,predictions))