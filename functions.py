import heapq
import random

def DM(stat):
    DMs = {0:-3,
           1:-2, 2:-2,
           3:-1, 4:-1, 5:-1,
           6:0, 7:0, 8:0,
           9:1, 10:1, 11:1,
           12:2, 13:2, 14:2,}
    if stat > 14: return 3
    else: return DMs[stat]

def roll_2D(boon):
    effect = 0
    if boon > 0:
        results = heapq.nlargest(2, [random.randint(1,6),random.randint(1,6),random.randint(1,6)])
    elif boon < 0:
        results = heapq.nsmallest(2, [random.randint(1,6),random.randint(1,6),random.randint(1,6)])
    else:
        results = [random.randint(1,6),random.randint(1,6)]

    effect = results[0] + results[1]
    return effect    

print(DM(10))