from glob import glob
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

import shutil

def duplicate_labels(images_list,path1,path2):
  images_box_map = defaultdict(list) #
  for x in images_list:
    img_without_extention = Path(x)
    image_label = os.path.join(path1, f'{img_without_extention.stem}.txt')
    image_label_f = os.path.join(path2, f'{img_without_extention.stem}'+'_b.txt')
    shutil.copyfile(image_label, image_label_f)

def duplicate_images(images_list,path1,path2):
  images_box_map = defaultdict(list) #
  for x in images_list:
    img_without_extention = Path(x)
    image = os.path.join(path1, f'{img_without_extention.stem}.jpg')
    image_f = os.path.join(path2, f'{img_without_extention.stem}'+'_b.jpg')
    shutil.copyfile(image, image_f)


to_add='./DWGAN_images/'
add_dir='./original_images/'
imgs = glob(to_add + "*.jpg")
imgs = [x for x in imgs ]


orig='./original_labels/'
all_test_labels = glob(orig + "*.txt")
test_labels = [x for x in all_test_labels ]
dest='./duplicated_labels/'


# duplicate_labels(test_labels, orig, dest)

duplicate_images(imgs, to_add, add_dir)
