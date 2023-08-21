import cv2
import numpy as np
from PIL import Image

def extract_features(image: Image.Image) -> np.ndarray:
    image_opencv = np.array(image)
    
    return image_opencv
