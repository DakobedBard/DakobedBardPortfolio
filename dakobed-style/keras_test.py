from keras.preprocessing.image import load_img, save_img, img_to_array
import numpy as np
from scipy.optimize import fmin_l_bfgs_b
from keras.applications import vgg19
from keras import backend as K
import logging


logging.info("KERAS INFO")
print("keras has been loaded..")