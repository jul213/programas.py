import numpy as np 

def add(x, y):
    return x + y

add = np.frompyfunc(add, 2, 1)