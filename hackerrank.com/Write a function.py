'''
Task
You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.
'''

def is_leap(year):
    leap = True
    not_leap = False
    # Write your logic here
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return leap
            return not_leap
        return leap


    return not_leap



year = int(raw_input())
print is_leap(year)