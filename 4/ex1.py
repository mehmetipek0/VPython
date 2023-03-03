import numpy as np
import math

def function(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        L = []
        for item in np.array(np.arange(2,n,0.5)):
            L.append(np.math.gamma(item+1))
        return L
print(function(7))


