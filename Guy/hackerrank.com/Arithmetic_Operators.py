'''
Task
Read two integers from STDIN and print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

Input Format
The first line contains the first integer, . The second line contains the second integer, .

'''


if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print a + b
if b > a:
    print b - a
else:
    print a - b

print a * b
