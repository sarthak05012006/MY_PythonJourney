import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,90])
reshaped_array = arr.reshape(3,3)
print(reshaped_array)
print(arr.ndim,"D")
print(reshaped_array.ndim,"D") 