import numpy as np
arr_1d = np.array([1,2,3,4,5,6])
arr_2d = arr_1d.reshape(3,2)
print("1D array : ",arr_1d)
print("Reshape array: ",arr_2d)

arr_3d = np.array([[[1,2,3,5],[4,5,6,2],[7,8,9,5]]])
print("3D array : ",arr_3d)
arr_reshape = arr_3d.reshape(4,3)
print(arr_reshape)