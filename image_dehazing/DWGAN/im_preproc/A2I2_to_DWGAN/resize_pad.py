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


def resize_pad_image(path1):

  img = cv2.imread(path1)
  img = cv2.resize(img, (1600, 750))

  old_image_height, old_image_width, channels = img.shape

  new_image_width = 1600
  new_image_height = 1200
  color = (255,255,255)
  result = np.full((new_image_height,new_image_width, channels), color, dtype=np.uint8)

  x_center = (new_image_width - old_image_width) // 2
  y_center = (new_image_height - old_image_height) // 2

  result[y_center:y_center+old_image_height, x_center:x_center+old_image_width] = img

  return result




def resize_pad_folder(path1,path2):

  hazy_images_cropped = [join(path1, f) for f in listdir(path1) if isfile(join(path1, f))]

  for image_path in hazy_images_cropped:
    #print(image_path)
    padded_image = resize_pad_image(image_path)
    #print(padded_image.shape)
    #cv2_imshow(hazy_image)
    name=os.path.basename(os.path.normpath(image_path))
    #print(write_path)
    cv2.imwrite(os.path.join(path2 , name), padded_image)



def resize_pad_folder(path1,path2):

  hazy_images_cropped = [join(path1, f) for f in listdir(path1) if isfile(join(path1, f))]

  for image_path in hazy_images_cropped:
    padded_image = resize_pad_image(image_path)
    name=os.path.basename(os.path.normpath(image_path))
    cv2.imwrite(os.path.join(path2 , name), padded_image)

input_train='./hazy_images_train'
output_train = './hazy_images_train_DWGAN'

input_test='./hazy_images_test'
output_test = './hazy_images_test_DWGAN'

resize_pad_folder(input_train,output_train)
resize_pad_folder(input_test,output_test)

