import cv2
import numpy as np

def calculate_similarity(features1: np.array, features2: np.array) -> float:

    difference = np.abs(features1[:,:,:3] - features2[:,:,:3])
    mean_difference = np.mean(difference)

    return mean_difference
    