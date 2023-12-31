import numpy as np
matrices = np.array([[1,2,5],[3,4,4]])
print("matrices : ",matrices)
print("elements : ",matrices.shape)
print("Dimension : ",len(matrices.shape))

#arange
print(np.arange(5))
print(np.arange(5,10))
print(np.arange(5,7,9))

#zeros
zero_arrays_1 = np.zeros([2])
print(zero_arrays_1)

zero_arrays_2 = np.zeros([2,3])
print(zero_arrays_2)

#ones
one_arrays_1 = np.ones([3])
print(one_arrays_1)

one_arrays_2 = np.ones([3,4])
print(one_arrays_2)

#using random
rand_arr = np.random.rand(5)
print(rand_arr)
print(rand_arr.shape)
print(len(rand_arr.shape))
print(len(rand_arr))

rand_arr2 = np.random.randint([1,5],[6,10])
print(rand_arr2)

rand_arr3 = np.random.rand(5, 5)
print(rand_arr3)
print(rand_arr3.shape)
print(rand_arr3.dtype)
