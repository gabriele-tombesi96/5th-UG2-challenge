This folder was built to perform some preprocessing on the images in order to adapt them to the format expected from DWGAN.

In particular the images had to be resize and then padded in `A2I2_to_DWGAN/`.

In the same way, the same operations were performed to turn DWGAN outputs back to the original shape and remove padding, in order for them to remain coherent with the corresponding labels in `DWGAN_to_A2I2/`.
