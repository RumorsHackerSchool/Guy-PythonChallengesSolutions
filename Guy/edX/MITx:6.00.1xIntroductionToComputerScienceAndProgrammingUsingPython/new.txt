# Type your code here
def max_of_even_value(list1):
    a1 = []
    for i in range(len(list1)):
        for num in list1[i]:
            a1.append(num)
    return even_num(a1)

def even_num(list1):
    even_num = []
    for i in list1:
        for n in list1:
            if i == n:
                even_num.append(n)
    return max_num(even_num)

def max_num(list1):
    while len(list1) != 1:
        list1.remove(min(list1))
    return list1


