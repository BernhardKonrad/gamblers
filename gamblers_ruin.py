# Write python script to simulate gambler's ruin

from random import random

initial = 10

moneyA = [initial]
moneyB = [initial]

while moneyA[-1] > 0 and moneyB[-1] > 0:
    if random() < 0.5:
        moneyA.append(moneyA[-1]+1)
        moneyB.append(moneyB[-1]-1)
    else:
        moneyA.append(moneyA[-1]-1)
        moneyB.append(moneyB[-1]+1)

print(moneyA, moneyB)
