'''
Problem 1
0.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5

'''
vowels = 'aeiou'
s = str(input("your string: "))
count = 0
for lop1 in vowels:
    for lop2 in s:
        if lop1 == lop2:
            count +=1

print (count)



