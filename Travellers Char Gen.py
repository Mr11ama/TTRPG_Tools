import random
from classes import Character
from functions import roll_2D

def TwoD_roll():
    return random.randint(2,12)

def Base_Stat_Gen(upper_lim,lower_lim):
    Raw_stats = [random.randint(lower_lim,upper_lim) for x in range(6)]
    stat_names = ["STR","DEX","END","INT","EDU","SOC"]
    for y in range(len(Raw_stats)):
        Base_stats = stat_names[y] +": "+str(Raw_stats[y])
        print(Base_stats)
    return Base_stats

#print(Base_Stat_Gen(12,2))
#print(roll_2D(0))

p1 = Character("Jimothy Jhalomet")
print(p1)
