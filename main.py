import math
import os
from pathlib import Path
import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage import img_as_float64
from skimage.filters import thresholding


def main(directory):
    for file in os.listdir(directory):
        file = directory.joinpath(file)


if __name__ == '__main__':
    path = Path(os.getcwd()).joinpath("assets")
    main(path)
