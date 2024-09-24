import numpy as np

## numpy version 
print(np.__version__)

arr = np.arange(1,10,2) #arange method is use to create array (start, stop, step)
print("Element of Array:", arr)

print()
## create array frome arr 
arr1= arr[np.array([4,0,2,-1])] #Indexing In 1D Array is [0,1,2,3,4.....]
print("Create Array From arr",arr1)

print()
## Indexinf In 2D Array 
arr = np.arange(12)
arr1= np.reshape(arr,(3,4))
print(arr1)
print(f"Element at oth row oth col is {arr1[0][0]}")
print(f"Element at 1th row 2th col is {arr1[1][2]}")

print()
## Indexing In 3D Array
arr1 = np.reshape(arr,(2,2,3))
print(arr1)
print(f"o th array 0 Row 2 element is {arr1[0, 0, 2]}")
print(f"o th array 1 Row 2 element is {arr1[0, 1, 1]}")
