import numpy as np
arr = np.array([10,20,30,40,50,60,70,80,90])
mask = arr > 40
print(arr[mask])
#or 
print(arr[arr>40])