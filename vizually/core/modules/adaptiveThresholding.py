 
import cv2
import numpy as np


def adaptiveThresholdingHandler(image: np.array, params: dict) -> np.array:
    """Adaptive Thresholding Handler
    Args:
        image(np.array): image to change
        params (dict): params has { threshold_value } range(about): (0, 2)
    Returns:
        np.array: thresholded image
    """

    if 'threshold_value' not in params:
        return image

    if params['threshold_value'] > 2 :
        params['threshold_value'] = 2
    elif  params['threshold_value'] < 0 :
        params['threshold_value'] = 0

    new_img = medianAdaptiveImageBinarizer(
        image, float(params['threshold_value']))
    return new_img


def medianAdaptiveImageBinarizer(image: np.array, thresh_value: float) -> np.array:
    """Binarize the image
    Args:
        image (np.array): image to change
        thresh_value (float): Threshold Value to choose
    Returns:
        np.array: binarized image
    """

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    medianGray = cv2.medianBlur(gray, 5)

    retImg = cv2.adaptiveThreshold(medianGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, thresh_value)

    return cv2.cvtColor(retImg, cv2.COLOR_GRAY2BGR)