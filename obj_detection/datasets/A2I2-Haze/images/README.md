# Trainind and Testing datasets for YOLOv5 fine-tuning and inference

-`test0/`* folder: test images directrly from dry-run, not dehazed. 
-`test1/`* folder:test images dehazed with pretrained FFA-net model (not finetuned on A2I2 dataset)
-`train0/`* folder: train images directly from haze_images, not dehazed 
-`train1/`* folder: train images (from haze_images folder)dehazed with pretrained-net model (not finetuned on A2I2 dataset)
-`train2/`* images: train images dehazed with DWGAN
-`train3/`* folder: augmented dataset = inital training set + DWGAN images
-`test2/`* folder: test images dehazed with DWGAN
-`train4/`* folder: train images dehazed with FFA-net
-`test4/`* folder: test images dehazed with FFA-net
-`train5/`* foler: train images dehazed with Aaecrnet (not finetuned)
-`test5/`* folder: test images dehazed with aecrnet (not finetuned)
-`train6/`* : original + DWGAN + FFA3

-`train/`*: augmented dataset of FFA + FFA1 + FFA2 + FFA3
-`test/`*: FFA3
