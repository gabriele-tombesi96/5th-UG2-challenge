In this folder, the training set of images provived by A2I2 is post-processed with the [crop.py](./crop.py) script in order to collect two dinstict sets of hazy images (`cropped_hazy_train/`)  and clean images (`cropped_clean_train/`), which are then used for dataset augmentation through image-dehazing.

In addition, the ground truth labels have to be converted to the format expected from YOLO_v5 in order to be able to fine-tune YOLO_v5. This is done with the script [reformat_labels.py](./reformat_labels.py).

Finally, the folder `AUGMENT/` contains some additional functions that are used to generate augmented datasets for YOLO_v5 finetuning assembling different datatest from previous preprocessing steps. In the example showed in the folder, the original training images and the DWGAN-dehazed training images are united in a single folder, and the correspongin labels are duplicated accordingly.
