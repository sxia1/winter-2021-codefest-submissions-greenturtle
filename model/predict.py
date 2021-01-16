import matplotlib.pyplot as plt
import numpy as np
import os
import PIL
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

model = tf.keras.models.load_model('model/my_model.h5')

def make_prediction(data):
    ###  IMAGE PREPROCESSING  ###

    #  data-->preprocessed_data #

    ###          END          ###

    print(data) 

    img_height = 180
    img_width = 180

    
    img_url = data 
    img_path = tf.keras.utils.get_file('someimage', origin=img_url)

    img = keras.preprocessing.image.load_img(
        img_path, target_size=(img_height, img_width)
    )
    img_array = keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0) # Create a batch

    prediction = model.predict(img_array)
    score = tf.nn.softmax(prediction[0])
    
    class_names=['daisy', 'dandelion', 'roses', 'sunflowers', 'tulips']
    
    print(score)
    # You may want to further format the prediction to make it more
    # human readable
    return {'prediction':prediction,'message':"This image most likely belongs to {} with a {:.2f} percent confidence.".format(class_names[np.argmax(score)], 100 * np.max(score))}
