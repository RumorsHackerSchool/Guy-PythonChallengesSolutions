import  binascii
import base64

file = open("/home/guy/Gits/PythonChallengesSolutions/Guy/CPChallenge/Networking-SniffingCap/data_websocket/unmask/test_.bin", "rb")
file2 = open("/home/guy/Gits/PythonChallengesSolutions/Guy/CPChallenge/Networking-SniffingCap/data_websocket/unmask/test_unmask32593608out.bin", "wb")

print(file)
lines = file.read()
print(lines)
#converted = binascii.b2a_uu(lines)
base_64_line = binascii.b2a_base64(lines)
print(base_64_line)
print (base64.b64decode(base_64_line))
file2.write(base64.b64decode(base_64_line))
file2.close()

a = lines
# binascii.b2a_uu takes at most 45 bytes at once
# this why i'm splitting the data into chunks of 45 bytes at most
b = [a[k:k+45] for k in range(0, len(a), 45)]

# You can also use:
# binascii.b2a_uu(k).decode('UTF8')
final = "".join(binascii.b2a_uu(k).decode('UTF8') for k in b)

print(final)


converted = binascii.b2a_uu(lines)
print(converted)
print (base64.b64decode(converted))