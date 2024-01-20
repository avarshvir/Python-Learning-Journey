import cv2
#read image
img1 = cv2.imread(r'..\python_14_opencv\images1\image1.png',0)

#save image
save = cv2.imwrite(r'..\python_14_opencv\images2\image1.png',img1)
print("Image is write", save)