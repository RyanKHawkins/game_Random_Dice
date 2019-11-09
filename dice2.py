import random

dice_rolls = []
def roll_dice(num):
    for die in num:
        roll = random.randint(1,6)
        dice_rolls.append(roll)
    
    return dice_rolls

print(roll_dice(2))