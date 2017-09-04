'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Sample Input

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

guy:
I need to user:
mycode = 'print "hello world"'
exec(mycode)
'''


if __name__ == '__main__':
    N = int(raw_input())
    def command(string):
        str2 = ''
        list2 = []
        for char in string:
            if char != ' ':
                str2+= char
            else:
                list2.append(str2)
                str2 = ''
        list2.append(str2)
        return list2


    list_made_by_user = []
    for loop in range(N):
        string = str(raw_input())
        if 'insert' in string:
            exec('list_made_by_user.insert(' + command(string)[-2] + ',' + command(string)[-1] + ')')
        elif 'remove' in string:
            exec('list_made_by_user.remove(' + command(string)[-1] + ')')
        elif 'append' in string:
            exec('list_made_by_user.append(' + command(string)[-1] + ')')
        elif 'sort' in string:
            exec('list_made_by_user.sort()')
        elif 'pop' in string:
            exec('list_made_by_user.pop()')
        elif 'reverse' in string:
            exec('list_made_by_user.reverse()')
        elif 'print' in string:
            exec('print list_made_by_user')
