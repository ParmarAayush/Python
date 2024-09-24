import numpy as np

#Slicing of 1D Array
arr = np.arange(6)
print(arr)
print(f"Slicing element of array {arr[1:5]}")

print()
# slicing of 2D array [row:row, col:row]
arr = np.arange(12)
arr1  = np.reshape(arr,(3,4))
print(arr1)
print()
print(arr1[0:3, 1:3])
print()
print(arr1[0:2, 1:3])