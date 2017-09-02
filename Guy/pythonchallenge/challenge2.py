checkfile = open("challenge2file.txt", 'r')
file = checkfile.read()
abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
print file

list1 = []
for lop in file:
    if lop in abc:
        list1.append(lop)

print ''.join(list1)
