'''
def func(x):
    x = x/2
    x = x ^ 2
    if (x and 255) > 83:
        x = x + 256
    x = x/2

    for lop in range(3):
        x = x * 2
        x = x - 1
        x = x / 4
        x = x ^ 2
    return x


def revers(x):
    for lop in range(3):
        x = x ^ 2
        x = x * 4
        x = x + 1
        x = x / 2

    x = x * 2
    if (x and 255) > 83:
        x = x - 256
    x = x ^ 2
    x - x * 2
    return x
'''
def func(x):
    x = x/2
    x = int(x)
    x = x ^ 2
    return x

def revers(x):
    x = x/2
    if type(x) == float:
        x = int(x)
        addOne = 1

    x = x ^ 2
    y = x ^ 2
    y = (y * 2) + addOne
    return x, y

def revers2(y):
    y = y ^ 2
    y = (y * 2) + 1
    return y

ans = func(255)
print(ans)
print(revers(255))
print(revers2(ans))