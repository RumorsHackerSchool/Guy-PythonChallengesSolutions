## this is for decoding base64 format
import base64
var1 = str(raw_input('Please type string for decoding in base64: '))
file = open("test.txt",'w')
file.write(base64.b64decode(var1))
print(base64.b64decode(var1))



