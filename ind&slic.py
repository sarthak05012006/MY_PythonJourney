#indexing and slicing
import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr[-2])
print(arr[4])
arr1 = np.array([[1,2,7],
                 [3,4,8],
                 [5,6,9]])
print(arr1[0,1])
print(arr1[1])
print(arr1[:,1])
print(arr[1:3])