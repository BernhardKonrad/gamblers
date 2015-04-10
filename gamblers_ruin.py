# Write python script to simulate gambler's ruin

from random import random

moneyA = 10
moneyB = moneyA

num_games = 0
while moneyA > 0 and moneyB > 0:
    if random() < 0.5:
        moneyA += 1
        moneyB -= 1
    else:
        moneyA -= 1
        moneyB += 1
    num_games += 1

print(moneyA, moneyB, num_games)
