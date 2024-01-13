# Solve the linear system Ax = B
import numpy as np
A = np.array([[2, 3], [4, 1]])
B = np.array([8, 7])

# Use np.linalg.solve to solve for x
x = np.linalg.solve(A, B)

print("Solution x:", x)