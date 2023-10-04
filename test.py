import random

def roll_dice(num):
    total = 0
    for i in range(num):
        total += random.randint(1,6)
    return total

print(roll_dice(2))