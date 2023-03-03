import math

x = [a*2*math.pi/50 for a in range(0,51)]

array = []

for item in x:
    y = int(50*math.sin(item))

    array.append(int(50*math.sin(item)))
    
    if(y==0):
        print("0")
    elif(y>0):
        print("+"*y)
    elif(y<0):
        print("-"*-y)
        array.sort()
print(array)

