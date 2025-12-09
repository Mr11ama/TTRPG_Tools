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