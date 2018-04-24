def func(x):
    x = x / 2
    x = int(x) ^ 951335252
    return x


def severs(x):
    x = x ^ 951335252
    x = x * 2
    return x

x = int(input("Please type number: "))
ans = func(x)
print(ans)
print(severs(ans))

#24393217.102564104