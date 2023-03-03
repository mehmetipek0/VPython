import numpy as np

f = open('file.txt','w')

for dimentions in np.arange(2,21,1):

    rands = np.array([np.random.uniform(0,1,dimentions*1000000)]).reshape(1000000,dimentions)

    hits = np.count_nonzero(1 > np.sqrt(np.power(rands,2).sum(axis=1)))
    
    calculatedVo = np.power(2,dimentions)*hits/1000000

    mathVo = np.power(np.pi,dimentions/2) / np.math.gamma(dimentions/2+1)
    
    print(str(dimentions)+') '+str(calculatedVo)+', '+str(calculatedVo/mathVo)+', '+str(hits)+'\n')
    f.write(str(dimentions)+') '+str(calculatedVo)+', '+str(calculatedVo/mathVo)+', '+str(hits)+'\n')

f.close()
