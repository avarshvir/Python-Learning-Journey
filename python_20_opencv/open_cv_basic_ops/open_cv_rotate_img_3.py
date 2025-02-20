import cv2
img = cv2.imread(r'..\python_14_opencv\images1\image1.png')

#get image height and width with the help of tuple unpacking
(h,w) = img.shape[:2]

#calculate the center of image
center = (w/2,h/2)

angle90 = 90
angle180 = 180
angle270 = 270

scale = 1.0

#rotating image 90 degree by clockwise
M = cv2.getRotationMatrix2D(center, angle90, scale)
rotated90 = cv2.warpAffine(img, M, (h, w))
cv2.imshow('90 degree',rotated90)
cv2.waitKey(0)
cv2.destroyAllWindows()

#rotating image 180 degree
M = cv2.getRotationMatrix2D(center,angle180,scale)
rotated180 = cv2.warpAffine(img,M,(h,w))
cv2.imshow('180 degree',rotated180)
cv2.waitKey(0)
cv2.destroyAllWindows()