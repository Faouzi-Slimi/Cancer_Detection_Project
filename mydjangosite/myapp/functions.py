import numpy as np
from django.shortcuts import render, redirect

def handle_uploaded_file(f):
    with open('myapp/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

import cv2
from os import path


import cv2
import keras
from PIL import Image
import os
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import model_from_json
def f_pred (path):
    img = np.asarray(Image.open(path))
    imgs=[]
    imgs.append(img)
    imgs = np.asarray(imgs)
    modelfile = open(r'C:\Users\Slimi Fawzi\Desktop\pythonProject3\mydjangosite\static\Model\model1.json','r')
    modeljson = modelfile.read()
    modelfile.close()
    model = model_from_json(modeljson)
    model.load_weights(r'C:\Users\Slimi Fawzi\Desktop\pythonProject3\mydjangosite\static\Model\model1.h5')



    return model.predict(imgs[0:1])[0][0] == 0.0
print(f_pred(r'C:\Users\Slimi Fawzi\Desktop\pythonProject3\mydjangosite\static\init\test_x_10.jpg'))

