#handling missing value
import numpy as np
arr = np.array([1,2,np.nan,3,np.nan])
print(np.isnan(arr))

cl_arr = np.nan_to_num(arr,nan=10)
print(cl_arr)