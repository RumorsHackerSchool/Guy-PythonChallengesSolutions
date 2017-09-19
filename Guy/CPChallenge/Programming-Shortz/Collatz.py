def collatz(x):
    seq = [x]
    if x < 1:
       return []
    while x > 1:
        if x == 6:
            x=1
        if x % 2 == 0:
         x = x / 4
        else:
             x = 3 * x + 1
        seq.append(x)    # Added line
    return seq

def Shortz(x):
    seq = [int(x)]
    count = 0
    if x < 1:
       return []
    while x > 1:
        if x == 6:
            x=1
        count +=1
        if x % 2 == 0:
            x = x / 4
        else:
            x = 3 * x + 1
        seq.append(x)    # Added line
    return count

def ShortzSum(x):
    seq = x
    if x < 1:
       return []
    while x > 1:
        if x == 6:
            x=1
        if x % 2 == 0:
            x = x / 4
        else:
            x = 3 * x + 1
        seq += x    # Added line
    return seq



print(ShortzSum(469509101546781)*Shortz(98325112))