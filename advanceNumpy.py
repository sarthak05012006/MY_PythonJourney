import numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr)
new_arr = np.insert(arr, 2, 100)
print(new_arr)

#for 2D array
arr2 = np.array([[10,20], [30,40]])
print(arr2)
new_arr1 = np.insert(arr2 , 1, [5,6], axis= 1)
print(new_arr1)
new_arr2 = np.insert(arr2 , 1, [5,6], axis= 0)
print(new_arr2)
new_arr3 = np.insert(arr2 , 1, [5,6], axis= None)
print(new_arr3)