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

def reformat_results(images_list,path1,path2):
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
      assert len(line_text) == 6, 'Each line must have 6 values' 
      coords = line_text[1:]
      a=[]
      a.append(round((2*1854*float(coords[0])-1854*float(coords[2]))/2,2))
      a.append(round((2*750*float(coords[1])-750*float(coords[3]))/2,2))
      a.append(round((2*1854*float(coords[0])+1854*float(coords[2]))/2,2))
      a.append(round((2*750*float(coords[1])+750*float(coords[3]))/2,2))
      a.append(round(float(coords[4]),3))
      of.write("vehicle ")
      for x in a:
          of.write(str(x) + " ")
      of.write("\n")
    of.close();

res = "./21-03/exp29/input"
ores = "./21-03/exp29/output"

all_im = glob(res+ "/*.txt")
all_im = [x for x in all_im ]

reformat_results(all_im,res, ores)
