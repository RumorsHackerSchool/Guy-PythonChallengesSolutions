checkfile = open("challenge3file.txt", 'r')
file = checkfile.read()
file2 = file.replace('\n', '')
print file2

count = 0

def checkletters(letters1, letters2):
    if letters1[0] in letters2 and letters1[1] in letters2 and letters1[2] in letters2:
        return True

def check3let(letters):
    len = len(letters)

list1 = []
for lop in file2:
    count += 1
    if file2[count-1].islower():
        if file2[count:count+3].isupper() and file2[count-4:count-1].isupper():
            if checkletters(file2[count:count+3], file2[count-4:count+1]):
                print 'yes'
                print file2[count-4:count+3]
                list1.append(file2[count-1])

print ''.join(list1)
