import math

f = open('file1.txt', 'w')

i=1
while i <= 10000000:
    sumOfNumbers = 0
    for j in range(1,i+1):
            
        div = j*2-1
        if(j%2 == 0):
            sumOfNumbers = sumOfNumbers + -1*(1/div)
        else:
            sumOfNumbers = sumOfNumbers+(1/div)
            
    calculatedPi = 4*sumOfNumbers            
    print(str(i)+') '+str(calculatedPi)+', '+str(calculatedPi/3.1415926536))
    f.write(str(i)+') '+str(calculatedPi)+', '+str(calculatedPi/3.1415926536)+'\n')
    if(i<100):
        i = i+1
    else:
        i = i*10

f.close()
