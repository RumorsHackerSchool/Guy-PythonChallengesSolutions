'''
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
'''

s = str(input("type your string: "))
s = s.lower()
find = 'bob'
count = 0

for lop in range(len(s)):
    if find == s[lop:lop+3]:
        count +=1


print(count)


