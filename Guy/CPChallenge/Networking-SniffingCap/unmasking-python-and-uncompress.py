

def input2hex(input):
    input = ' ' + input
    input = input.replace(' ', ',0x')
    input = input[1:]
    list1 = []
    newStr = ''
    for loop in input:
        if loop == ',':
            list1.append(hex(int(newStr,16)))
            newStr = ''
        else:
            newStr += loop
    list1.append(hex(int(newStr, 16)))
    print(type(list1[0]))
    return list1

def xor(a, b):
    ans = int(a, 0) ^ int(b, 0)
    return hex(ans)


if __name__ == "__main__":
    key = str(input('Please enter your key (must be hex format):'))
    payload = str(input('Please enter your payload (must be hex format):'))
    keyList = input2hex(key)
    payloadList = input2hex(payload)

    print(keyList)
    print(payloadList)
    count = 0
    newList = []
    str = ''
    for loop in range(len(payloadList)):
        if count == 4:
            count = 0
        newList.append(xor(keyList[count], payloadList[loop]))
        #str += str(xor(keyList[count], payloadList[loop]))
        count +=1
    newList.append(xor(keyList[count], payloadList[loop]))
    for loop in range(len(payloadList)):
        if len(newList[loop]) == 3:
            newStr = newList[loop][0:2] + '0' + newList[loop][-1]
            str += newStr.replace('0x', '')
        else:
            str += newList[loop].replace('0x', '')
    print(str)

#!/usr/bin/env python3
import zlib

websocket_payload_packet_1 = bytes.fromhex(str.replace("\n", ""))


# Data from frame 1
data = websocket_payload_packet_1
# Needed per spec (https://tools.ietf.org/html/rfc7692#section-7.2.2)
data += b'\0\0\xff\xff'


z = zlib.decompressobj(wbits=-15)
out = z.decompress(data)
print(out)