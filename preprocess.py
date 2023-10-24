# imports
import cv2
import numpy as np
import os
from urllib.request import urlopen, Request

# local imports
import params as p

# helper functions
def load_image(path, isURL):
    if isURL:
        # load image from URL
        try:
            with urlopen(Request(path, headers={'User-Agent': 'Mozilla'})) as url:
                arr = np.asarray(bytearray(url.read()), dtype=np.uint8)
                image = cv2.imdecode(arr, -1) # 'Load it as it is'
        except:
            image = None
    else:
        # load local image
        image = cv2.imread(path)

    if image is None:
        print(f'{p.ERROR_PREFIX(os.path.basename(__file__))} unable to find the {"image at URL:" if isURL else "local image:"} {path}')
        return
    return image

def filter_image(image):
    """
    convert RGB to grayscale 'pixel' value, then:
    pixel' = alpha*pixel + beta
        alpha = contrast filter value
        beta = brightness filter value
    
    alpha and beta are assigned in a global params property file

    NSTC Formula for grayscale according to:
        https://support.ptc.com/help/mathcad/r9.0/en/PTC_Mathcad_Help/example_grayscale_and_color_in_images.html
    """
    grayscale = 0.299*image[:,:,0] + 0.587*image[:,:,1] + 0.114*image[:,:,2]
    filter = p.alpha*grayscale - p.beta
    filter[filter>255] = 255
    filter[filter<0] = 0
    filter = filter.astype("uint8")
    return filter