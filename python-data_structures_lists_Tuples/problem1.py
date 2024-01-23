import random
import math

# generate a random list of 5 values
numList = []

for i in range(5):
    numList.append(random.randrange(1, 9))
for i in numList:
    print(i)
