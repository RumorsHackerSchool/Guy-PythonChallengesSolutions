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