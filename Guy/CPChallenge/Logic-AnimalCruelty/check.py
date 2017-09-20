'''
def func(x):
        x = x / 2
        x = xor(x, 951335252)

        if (x & 255) > 83:
            x = x + 256
        x = x / 39

        do 3 times:
            x = x * 33
            x = x - 1
            x = x / 4
            x = xor(x, 89)

        return x
//end of func(x)

func()

'''

def func(x):
    x - x/2
    x = x ^ 951335252
    if (x and 255) > 83:
        x = x + 256
    x = x/39

    for lop in range(3):
        x = x * 33
        x = x - 1
        x = x / 4
        x = x^ 89
    return x

test = open('test.txt', 'w')
lop = 0

while True:
    lop +=1
    x = int(str(lop) + '002')
    ans = func(x)
    print("the x is, ", x,"and the ans in func is, ",ans)
    if func(x) == 27750:
        print("I found the ans!!! x is " + str(x))
        break

    x = int('-' + str(lop) + '002')
    ans = func(x)
    print("the x is, ", x,"and the ans in func is, ",ans)
    if func(x) == 27750:
        print("I found the ans!!! x is " + str(x))
        break
