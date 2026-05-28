import numpy as np
arr = np.array([1,2,3,4,5,6])
new_arr = np.delete(arr,1)
print(new_arr)
arr2 = np.array([[1,2,3],[4,5,6]])
new_arr2 = np.delete(arr2, 1 ,axis= 1)
print(new_arr2)