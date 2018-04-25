binary = open("./binary.txt", 'r')
file = binary.read()
newfile = open("newfile.txt", 'w')

for loop in file:
    if loop != "!":
        newfile.write(loop)
        print(loop)
    else:
        continue



