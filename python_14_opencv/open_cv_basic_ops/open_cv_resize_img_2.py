import cv2
img = cv2.imread(r'..\Python-Learning-Journey\python_14_opencv\images1\image1.png',1)
scale = 60
#scale2 = 160

#width = int(img.shape[1])  #-> not changing width
width = int(img.shape[1]*scale/100)

#height = int(img.shape[0])   #-> not changing height
height = int(img.shape[0]*scale/100)
dim = (width,height)
#cv2.imshow('kk',img)

#resize image
resize_img = cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
print('Resized Dimensions : ',resize_img.shape)
cv2.imshow('Resized Image',resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()