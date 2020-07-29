import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('bus.jpg')
plt.imshow(img)

sobel = cv2