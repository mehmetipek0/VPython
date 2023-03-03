import random
import time

print(" "*17+"START\n")
locationOfStar = 18;
print("|"+" "*locationOfStar+"*"+" "*(36-locationOfStar)+"|"+str(locationOfStar-18))
flipCount = 0
while(locationOfStar != 36 and locationOfStar != 0):
    move = random.choice([-1,1])
    flipCount += 1
    locationOfStar = locationOfStar + move;
    print("|"+" "*locationOfStar+"*"+" "*(36-locationOfStar)+"|"+str(locationOfStar-18))
    time.sleep(0.02)
print("coin flipped "+str(flipCount)+" times!")
