import numpy as np
arr1 = np.array([1,2,3,4])
arr2 = np.array([1,2,3,4])
arr3 = arr1 @ arr2
print(arr3)

arr4 = np.array([[1,2],[2,3]])
arr5 = np.array([[5,6],[7,8]])
arr6 = arr4 @ arr5
print(arr6)
arr7 = np.array([1,2])
arr8 = arr6 @ arr7
print(arr8)