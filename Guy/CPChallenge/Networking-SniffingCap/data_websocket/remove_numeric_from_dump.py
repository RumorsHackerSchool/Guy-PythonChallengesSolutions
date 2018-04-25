file = open("dump.txt", "r")
string = ''
for loop in range(1000):
    string += file.readline()[7:].replace('\n', ' ')
print(string)