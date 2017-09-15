'''
Problem 3
0.0/15.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which
the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage
you to work smart. If you've spent more than a
few hours on this problem, we suggest that you
move on to a different part of the course.
If you have time, come back to this problem
after you've had a break and cleared your head.

'''

s = str(input("type your string: "))
s = s.lower()
alphabetical = 'abcdefghijklmnopqrstuvwxyz'

def isInAlphabeticalOrder(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
        else:
            return True


def check_lest_letter(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
        else:
            return True

list1 = []
string1 = ''

for lop in range(len(s)):
    if isInAlphabeticalOrder(s[lop:]):
        print ('in the lop')
        print (s[lop])
        string1 += s[lop]
    elif s[lop] > s[lop-1]:
        string1 += s[lop]
        print("in the elif")
        list1.append(string1)
        string1 = ''
    else:
        print('in the else')
        print(string1)
        string1 += s[lop]
        list1.append(string1)
        string1 = ''
        print(string1)

print(string1)
print (list1)

print('check')
maxlength = max(len(check_longest) for check_longest in list1)
longest_strings = [s for s in list1 if len(s) == maxlength]
if len(longest_strings) > 1:
    longest_strings = longest_strings[0]
else:
    longest_strings = ''.join(longest_strings)

print ('Longest substring in alphabetical order is: ', longest_strings)