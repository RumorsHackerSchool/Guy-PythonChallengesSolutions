'''
def func(x):

    x = x/2
    x = x ^ 951335252
    if (x and 255) > 83:
        x = x + 256
    x = x/39

    for lop in range(3):
        x = x * 33
        x = x - 1
        x = x / 4
        x = x ^ 89
    return x
'''
def check_dechimal(x):
    string = str(x)
    if 0 == int(string[string.find('.')+1:]):
        return(int(x), 1)
    float_num = x
    len_of_num_after_point = len(string[string.find('.')+1:]) # this will bring the len after ".'
    newString = string.replace(".", '')
    division_num_after_func = '1' + ('0' * len_of_num_after_point) # divition num to for futer use (make to Decimal)
    return (int(newString), int(division_num_after_func))

def func(x):

    x = x/2
    if type(x) == float:
        x = check_dechimal(x)[0]
        division = check_dechimal(x)[1]

    x = x ^ 951335252
    x = x / division
    print(x)
    if (x and 255) > 83:
        x = x + 256
    x = x/39

    for lop in range(3):
        x = x * 33
        x = x - 1
        x = x / 4

        if type(x) == float:
            x = check_dechimal(x)[0]
            division = check_dechimal(x)[1]

        x = x ^ 89

        x = x / division

    return x


for lop in range(10000000000000000000000000000000000):
    print(lop)
    print(func(lop))
