#accessing and modifying pixel values
import numpy as np
import cv2
img = cv2.imread(r'E:\Python Project\Python Learning Journey\Python-Learning-Journey\python_14_opencv\images1\image1.png',1)
print(img.shape)

pixel = img[10,18]
print(pixel)

#accessing image properties
#height, width, numbers of channel in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
size1 = img.size

print('Image Height :', height)
print('Image Width :',width)
print('Number of channels :',channels)
print('Image Size :',size1)

#spliting and merging image channel
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
