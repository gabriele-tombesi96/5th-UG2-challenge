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


def get_hazy_image(img_path):
  img = cv2.imread(img_path)
  cropped_image = img[:int(img.shape[0]/2)]
  return cropped_image

def get_clean_image(img_path):
  img = cv2.imread(img_path)
  clean_image = img[int(img.shape[0]/2):]
  return clean_image

def crop_folder(img_list, path, clean=0):
  for image_path in img_list:
    if clean == 0:
      image = get_hazy_image(image_path)
    else:
      image = get_clean_image(image_path)
    name=os.path.basename(os.path.normpath(image_path))
    cv2.imwrite(os.path.join(path , name), image)


path='./hazy_clean_train'
images = [join(path, f) for f in listdir(path) if isfile(join(path, f))]

crop_folder(images, './cropped_hazy_train')
crop_folder(images, './cropped_clean_train', 1)
