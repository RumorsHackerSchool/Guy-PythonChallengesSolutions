'''

Read an integer .

Without using any string methods, try to print the following:


Note that "" represents the values in between.

Input Format
The first line contains an integer .

'''

from __future__ import print_function
if __name__ == '__main__':
    n = int(raw_input())
    list1 = []
    for i in range(1, n+1):
        list1 += str(i)
    print (''.join(list1))
