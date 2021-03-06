import cv2
import numpy as np
from skimage.filters import meijering, sato, frangi, hessian


def ridgeDetectorHandler(image: np.array, params: dict) -> np.array:
    """Ridge Detector Handler

    Args:
        image(np.array): image to change
        params (dict): params has { apply: bool }

    Returns:
        np.array: Ridges present in the image
    """

    if 'apply' not in params or params['apply'] is False:
        return image
    
    new_img = hessianRidgeDetector(
        image)
    return new_img


def hessianRidgeDetector(image: np.array) -> np.array:
    """Find the ridges in the image

    Args:
        image (np.array): image to change

    Returns:
        np.array: All the ridges are white in color and the remaining image is black
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    retImg = meijering(gray)
    retImg = np.stack((retImg, ) * 3, axis = -1)
    retImg = (retImg*255).astype(np.uint8)
    return retImg