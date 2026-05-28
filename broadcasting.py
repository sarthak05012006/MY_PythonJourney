import numpy as np
prices = np.array([100,200,300])
discount = 10
final_prices = prices - (prices * discount/100)
print(final_prices)

arr = np.array([10,20,30])
result = arr * 2
print(result)

matrix = np.array([[10,20,30], [40,50,60]])
vector = np.array([1,1,1])

result2 = matrix + vector
print(result2)

mat = np.array([1,2])

reshape_aa = mat.reshape(2,1)
result3 = matrix + reshape_aa
print(result3)
