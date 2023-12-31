import numpy as np
arr1 = np.array([0,1,2,3,4,5,6,7,8,9,10])
print(arr1[2:7])
print(arr1[2:])
print(arr1[:7])
print(arr1[-1])
print(arr1[-5:-1])
print(arr1[-1:-5])   #---> [] empty
print(arr1[-1:])
print(arr1[:-1])

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2[0][1])
print(arr2[1])
print(arr2[:3][:3])