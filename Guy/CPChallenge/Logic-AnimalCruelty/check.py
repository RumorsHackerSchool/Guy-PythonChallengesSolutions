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
        x - x+ 256
    x = x/39

    for lop in range(3):
        x = x * 33
        x = x - 1
        x = x / 4
        x = x^ 89
    return x

test = open('test.txt', 'w')


for lop in range(0, 999999999):
    x = int(str(lop) + '002')
    print("the x is, ", x,"and the ans in func is, ",func(x))
    test.write("the x is, ", x,"and the ans in func is, ",func(x))
    if func(x) == 27750:
        print("I found the ans!!! x is " + str(x))
        test.write("I found the ans!!! x is " + str(x))
        break
