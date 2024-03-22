import os
from PIL import Image
import numpy as np
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model


class ModelPredict:

 def __init__(self) -> None:
#   modelpath = os.getcwd()+'/model/HCC_B4_01.h5'
  modelpath = os.getcwd()+'/hcc_v01/model/HCC_B4_01.h5'
# ******
# ******  
  self.__model = load_model(modelpath)
 
 def load_image(self):
    
    patient_img_temp = os.getcwd()+'/hcc_v01/assets/' + 'patientIMG.jpeg' # this is the source of the asset folder
    img = load_img(patient_img_temp, target_size=(200, 200, 1), color_mode='grayscale')
    img = img_to_array(img)
    img = img.reshape(1, 200, 200, 1)
    predictCase = self.__model.predict(img)[0][0]
    return predictCase