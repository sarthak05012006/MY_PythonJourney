import numpy as np
"""
stacking
vertical , horizontal
vstack() row wise
hstack() coloumn wise

splitting 
np.hsplit()
np.vsplit()


"""
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.vstack((arr1, arr2)))
print(np.hstack((arr1, arr2)))

arr = np.array([1,2,3,4,5,6])
print(np.split(arr,2))