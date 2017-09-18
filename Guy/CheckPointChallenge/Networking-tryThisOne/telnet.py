import telnetlib

def parse_rpn(expression):
    """ Evaluate a reverse polish notation """
    """ cresit to danishmujeeb """
    stack = []
    for val in expression.split(' '):
        if val in ['-', '+', '*', '/', '^']:
            op1 = stack.pop()
            op2 = stack.pop()
            if val == '-': result = op2 - op1
            if val == '+': result = op2 + op1
            if val == '*': result = op2 * op1
            if val == '/': result = op2 / op1
            if val == '^': result = op2 ** op1
            stack.append(result)
        else:
            stack.append(int(val))
    return stack.pop()

checkThis = 0
tn = telnetlib.Telnet("35.158.25.165", "10111")
while True:
    line = tn.read_until("\n")  # Read one line
    try:
        if type(int(line[0]))==int:
            print(line)
            print("check")
            checkThis = line
            print(checkThis.encode('ascii'))
            print(type(int(checkThis.encode('ascii'))))
            print(parse_rpn(checkThis).encode('ascii'))

    except ValueError:
        continue
