import numpy as np
list1 = [1,2,3,4]
list2 = [5,6,7,8]
arr1 = np.array(list1)
arr2 = np.array(list2)

#addition
result_addition = arr1 + arr2
print("Addition : ",result_addition)

#subtraction
result_subtraction = arr1 - arr2
print("Subtraction : ",result_subtraction)

#multiplication
result_multiplication = arr1 * arr2
print("Multiplication : ",result_multiplication)

#division
result_division = arr1/arr2
print("Division : ",result_division)

#modulus
result_modulus = arr1 % arr2
print("Modulus : ",result_modulus)

#dot product
dot_product = np.dot(arr1, arr2)
print("Dot Product : ",dot_product)