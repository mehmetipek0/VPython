import numpy as np

for n in np.arange(2,6,1):
    c = np.array(np.arange(1,151,1))
    for i in c:
        b = np.array(np.arange(1,i,1))
        for j in b:
            a = np.array(np.arange(1,j,1))
            for k in a:
                if(np.power(k,n) + np.power(j,n) == np.power(i,n) and k < j):
                    print("n="+str(n)+")"+str(k) +" "+ str(j) +" "+ str(i))
        




