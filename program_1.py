#Random Dice
#Samuel Renneke, 2/19/2026

import random

def randDice():

    n1 = random.randint(1,6)
    n2 = random.randint(1,6)

    return n1 + n2


total = 0

for i in range(101):
    value = randDice()
    total = total + value

average = total / 100
print(average)
