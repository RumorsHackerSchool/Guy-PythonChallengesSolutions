

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
    print(type(a))
    return hex(hex(a) ^ hex(b))


if __name__ == "__main__":
    key = str(input('Please enter your key (must be hex format):'))
    payload = str(input('Please enter your payload (must be hex format):'))
    keyList = input2hex(key)
    payloadList = input2hex(payload)

    print(keyList)
    print(payloadList)
    count = 0
    str = ''
    print(type(keyList[0]))
    for loop in range(len(payloadList)):
        if count == 4:
            count = 0
        str += str(hex(xor(keyList[count], payloadList[loop])))
        count +=1
    str.replace('0x', '')
    print(str)

