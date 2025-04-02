import numpy as np 

def add(x, y):
    return x + y

add = np.frompyfunc(add, 2, 1)

print(add([1,2,4], [5,6,7]))
print(type(add))