#poperties of numpy
import numpy as np
arr_2d = np.array([[1,2,3],
                   [4,5,6]])

print(arr_2d.shape)
print(arr_2d.size)
print(arr_2d.ndim)
print(arr_2d.dtype)
arr_int = arr_2d.astype(float)
print(arr_int.dtype)
print(arr_2d + 3)