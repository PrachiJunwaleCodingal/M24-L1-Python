#operation by numby

import numpy as np
matx = np.arange(9, dtype=float).reshape(3, 3)
print("Matrix:")
print(matx)
arrA = np.array([5,5,5])
print("\nArray:", arrA)

print("Elementwise operation are as:")
print("\naddition:")
print(np.add(matx, arrA))
print("\nsubtraction:")
print(np.subtract(matx, arrA))
print("\nmultiplication:")
print(np.multiply(matx, arrA))
print("\ndivision:")
print(np.divide(matx, arrA))
