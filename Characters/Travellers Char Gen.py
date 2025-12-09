import random

def TwoD_roll():
    return random.randint(2,12)

def Base_Stat_Gen(upper_lim,lower_lim):
    Raw_stats = [random.randint(lower_lim,upper_lim) for x in range(6)]
    stat_names = ["STR","DEX","END","INT","EDU","SOC"]
    for y in range(len(Raw_stats)):
        Base_stats = stat_names[y] +": "+str(Raw_stats[y])
        print(Base_stats)
    return Base_stats

class Career:
    Past_Career_Quantity = 0
print(Base_Stat_Gen(12,2))

class Character:
    STR = 0
    DEX = 0
    END = 0
    INT = 0
    EDU = 0
    SOC = 0
    NAME = ""
    RACE = "Human"
    CAREER = Career

    
