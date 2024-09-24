import os
import numpy as np 

arr = np.array([1,2,3,4])
print(arr.dtype)
print(f"{arr.ndim}D Array => {arr}")
np.save("outfile", arr) ## save file
np.savetxt("outfiletxt.txt", arr) ## save file


# structure is (tuple)>[martix]>[row]
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"\n{arr.ndim}D Array =>\n {arr}")

arr = np.array([ [ [1, 2, 3], [4, 5, 6] ], [ [1, 2, 3], [4, 5, 6] ] ])
print(f"\n{arr.ndim}D Array =>\n {arr}") ## ???

## Reconstruct array from save file
# os.chdir("/media/HDD1/Courses/Python/Library/Numeric_Python")

newArr = np.load("outfile.npy")
print(f"New Constructed array=>{newArr}")

newArr = np.loadtxt("outfiletxt.txt")
print(f"New Constructed array=>{newArr}")