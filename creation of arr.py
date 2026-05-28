import numpy as np
ar_1d = np.array([10,20,30,40,50])
print(ar_1d)
arr_2d = np.array([[10,20,30],
                   [40,50,60],
                   [70,80,90]])

print(arr_2d)
print(type(arr_2d))
print(np.zeros(10))
filled_arr = np.full((2,2),5)
print(filled_arr)
arr = np.arange(1,16,2)
print(arr)
id_mt = np.eye(3)
print(id_mt)