import numpy as np


x = np.array([
    [1,2,3],
    [2,3,4],
    [3,4,5],
    [4,5,6],
])

w = np.array([10,20,30])

y = np.zeros(x.shape)

# x.shapre returns the number of rows anc olumns in a tuple
# So x.shape[0] is the number of rows
for i in range(x.shape[0]): 
    y[i,:] = x[i,:] + w

print(y)

# This solution works, but its slower

# Broadcasting

z = x + w
print(z)