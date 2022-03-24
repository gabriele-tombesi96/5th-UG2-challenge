# 5th-UG2-challenge

Please read [the report](/report.pdf) available in the home folder of this repository for a better explanation regarding this project.

## Object Detection
- [yolo_v5](https://github.com/gabriele-tombesi96/5th-UG2-challenge/tree/main/obj_detection/yolov5) is the chosen model
- Created custom fine-tuning dataset based on the training and dry-run set collected from the A2I2 dataset
  - Pre-processing step of the label files in order to comply with the bounding boxes coordinates format expected by the network
  - Created a custom configuration file for the dataset, in order to set the correct paths to the folders containing images and labels
-  Enabled the W&B flow for real time visualization and cloud logging, in order to be able to have a better overview of the QoR of each fine-tuning attempt.
-  Several fine-tuning attempts playing with some of the hyperparameters leveraged by yolo_v5. Optimal choice:
   -  50 epochs
   -  batch_size=32

Training results summary
[training](/figures/1.png)

Example of object detection on test images
[objdetect](/figures/2.png)
