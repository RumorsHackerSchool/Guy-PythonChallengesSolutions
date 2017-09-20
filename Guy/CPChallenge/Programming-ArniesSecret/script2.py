import binascii


newfile = open("newfile.txt", 'r')
thefile = newfile.read()
thefile=thefile.split()

file2 =open("file2.txt", 'w')
string = '0b'
binNum = 0
print(thefile)
for loop in thefile:
    if loop == "ZERO":
        binNum=0
        string += str(binNum)
        file2.write(str(binNum))
        print(binNum)
    elif loop == "ONE":
        binNum=1
        string += str(binNum)
        file2.write(str(binNum))
        print(binNum)
    else:
        print(loop)

print(string)
n = int(string, 2)
print(binascii.b2a_base64(n[2:]))


def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

print decode_binary_string(string)