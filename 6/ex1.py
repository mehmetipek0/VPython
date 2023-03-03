import numpy as np
import matplotlib.pyplot as plt

"""
rands = np.random.randint(1,100,1000000)
print(rands)
"""

x = 0;
y = 0;
xlist = [0]
ylist = [0]
for i in np.arange(0,10**6+1):
    rand = np.random.randint(0,100)
    x_ = x
    y_ = y
    if(rand<85):
        x = ((0.85*x_)+(0.04*y_))
        y = ((-0.04*x_)+(0.85*y_)+1.6)
    elif(rand<92):
        x = ((0.2*x_)-(0.26*y_))
        y = ((0.23*x_)+(0.22*y_)+1.6)
    elif(rand<99):
        x = ((-0.15*x_)+(0.28*y_))
        y = ((0.26*x_)+(0.24*y_)+0.44)
    else:
        x = 0
        y = 0.16*y_
    xlist.append(x)
    ylist.append(y)


plt.plot(xlist,ylist,',')
#plt.savefig('fractal.png',format='png',dpi=400)
plt.axis([1,2,6,7])
plt.show()



