import numpy as np

n = 2;

rands = np.random.randint(1,367,n*1000).reshape(1000,n)
print(rands)
print(rands[ : , 0:1])
print(rands[ : , 1:2])
print(rands[ : , 0:1] - rands[ : , 1:2])
print(1000-np.count_nonzero(rands[ : , 0:1] - rands[ : , 1:2]))


    
