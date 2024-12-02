import numpy as np

x = np.array([1,2,3])
w = np.array([[1,1,1],[2,2,2]])

b = np.array([1,2])
# print(np.matmul(x,np.rot90(w)) + b)


#------------------#
#        ┌     ┐
# [1 2 3]│ 1 2 │ + [1 2] = [7 14]
#        │ 1 2 │
#        │ 1 2 │
#        └     ┘
#------------------#

print(np.zeros((3,2)))
print(np.rot90(w))