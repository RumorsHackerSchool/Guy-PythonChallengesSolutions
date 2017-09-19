def collatz_sequence(x):
    seq = [int(x)]

    if x < 1:
       return []
    while x > 1:
       if x % 4 == 0:
         x = x / 4
       else:
         x = 3 * x + 1
       seq.append(x)    # Added line
    return seq

print(collatz_sequence(5))