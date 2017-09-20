def func(x):
    x - x/2
    x = x ^ 2
    if (x and 255) > 83:
        x - x + 256
    x = x/2

    for lop in range(3):
        x = x * 2
        x = x - 1
        x = x / 4
        x = x ^ 2
    return x

print func(255)