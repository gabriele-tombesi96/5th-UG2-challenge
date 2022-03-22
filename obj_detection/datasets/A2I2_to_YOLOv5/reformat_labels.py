from pathlib import Path
from glob import glob
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


def reformat_labels(images_list,path1,path2):
  images_box_map = defaultdict(list)
  for x in images_list:
    img_without_extention = Path(x)
    image_label = os.path.join(path1, f'{img_without_extention.stem}.txt')
    image_label_f = os.path.join(path2, f'{img_without_extention.stem}.txt')
    f = open(image_label, "r")
    of= open(image_label_f, "w")
    lines = f.read().strip().split('\n')
    for line in lines:
      line_text = line.strip().split(' ')
      assert len(line_text) == 5, 'Each line must have 5 values' 
      coords = line_text[1:]
      a=[]
      a.append((int(coords[0])+int(coords[2]))/(2*1854))
      a.append((int(coords[1])+int(coords[3]))/(2*750))
      a.append((int(coords[2])-int(coords[0]))/1850)
      a.append((int(coords[3])-int(coords[1]))/750)
      of.write("0 ")
      for x in a:
          of.write(str(round(x,6)) + " ")
      of.write("\n")
    of.close();


all_images = glob("./hazy_clean_train/*.jpg")
train_images = [x for x in all_images]

in_path='./haze_train_labels'
out_path='./haze_train_labels_YOLO'
reformat_labels(train_images,in_path,out_path) 
