from random import random
totalThrows = 10^4
validThrows = 0
for i in range(totalThrows) :
    #   Generatint random numbers
    r = random()
    x = -1 + 2 * r
    r = random()
    y = -1 + 2 * r
    # Checking ponits
    if x * x + y * y <= 1 :
        validThrows += 1
# 
pi = 4.0 * validThrows / totalThrows
print("The estimated pi is :", pi)



