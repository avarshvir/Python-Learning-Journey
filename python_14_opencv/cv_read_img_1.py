import cv2
img = cv2.imread(r'..\python_14_opencv\images1\image1.png',1)
cv2.imshow('image1',img) #for displaying image
cv2.waitKey(300)
cv2.destroyAllWindows()