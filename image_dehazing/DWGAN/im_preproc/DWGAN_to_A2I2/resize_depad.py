from pathlib import Path
from random import choice, sample
from pathlib import Path
from collections import defaultdict
from keras.preprocessing import image
import os
from os import listdir
from os.path import isfile, join
import cv2
import numpy as np
import imutils
from PIL import Image
from numpy import asarray

def resize_depad_image(path1):
  image = cv2.imread(path1)
  img = asarray(image)
  old_image_height, old_image_width, channels = img.shape

  new_image_width = 1600
  new_image_height = 750

  x_center = (old_image_width - new_image_width) // 2
  y_center = (old_image_height - new_image_height) // 2

  img = img[y_center:y_center+new_image_height, x_center:x_center+new_image_width]

  result = cv2.resize(img, (1853, 750))

  return result



def resize_depad_folder(path1,path2):
  hazy_images_cropped = [join(path1, f) for f in listdir(path1) if isfile(join(path1, f))]
  for image_path in hazy_images_cropped:
    padded_image = resize_depad_image(image_path)
    name=os.path.basename(os.path.normpath(image_path))
    name=name.replace('pred_', '')
    cv2.imwrite(os.path.join(path2 , name), padded_image)


output_train='./hazy_images_train1_DWGAN'
output_train_A2I2 = './hazy_images_train1'

output_test='./hazy_images_test1_DWGAN'
output_test_A2I2 = './hazy_images_test1'

resize_depad_folder(output_train,output_train_A2I2)
resize_depad_folder(output_test,output_test_A2I2)
