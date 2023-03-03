import math

def fun(number):
    
    if number < 0:
        return 0
    elif number == 0:
        return 1
    elif number == 1:
        return 1
    else:
        counter = 1        
        while(number>0.5):
             counter = counter*number
             number = number-1         
        if(number == 0.5): 
            counter = counter*((math.sqrt(math.pi))/2)
        
    print(counter)  

fun(1.5)
fun(2.5)
fun(6)
