import random
import math

f = open('file2.txt','w')

i = 1
while i <= 10000000:
    circleHit = 0
    if(i<100):  
        for j in range(1,i+1):
            randomX = random.random()
            randomY = random.random()
            #print(i)
            if math.sqrt(randomX**2+randomY**2) < 1:
                circleHit = circleHit + 1
                
        calculatedPi = 4*(circleHit/i)
        print(str(i)+') '+str(calculatedPi)+', '+str(calculatedPi/3.1415926536))
        f.write(str(i)+') '+str(calculatedPi)+', '+str(calculatedPi/3.1415926536)+'\n')
##        f.write('Hello')
        i = i+1
    else:
        for j in range(1,i+1):
            randomX = random.random()
            randomY = random.random()
            #print(i)
            if math.sqrt(randomX**2+randomY**2) < 1:
                circleHit = circleHit + 1
                
        calculatedPi = 4*(circleHit/i)        
        print(str(i)+') '+str(calculatedPi)+', '+str(calculatedPi/3.1415926536))
        f.write(str(i)+') '+str(calculatedPi)+', '+str(calculatedPi/3.1415926536)+'\n')
        i = i*10
    
f.close()
