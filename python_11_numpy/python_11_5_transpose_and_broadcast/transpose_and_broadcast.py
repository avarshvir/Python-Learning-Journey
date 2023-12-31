import numpy as np
#transpose
arr1 = np.array([[1,2],[3,4]])
print("before transpose : ",arr1)
print("after transpose : ",arr1.T)
#broadcast
arr2 = np.array([[1,2,3,4],[1,2,3,4],[5,6,7,8],[5,6,7,8]])
arr3 = np.array([1,2,3,4])
arr4 = arr2 + arr3
print(arr4)