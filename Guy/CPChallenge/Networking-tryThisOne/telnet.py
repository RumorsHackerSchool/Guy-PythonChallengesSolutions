import telnetlib

def parse_rpn(expression):
    """ Evaluate a reverse polish notation """
    # credit to danishmujeeb
    stack = []
    for val in expression.split(' '):
        if '\n' in val:
            val= val[0]
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
file = open('file.txt', 'w')
while True:
    line = tn.read_until("\n")  # Read one line
    try:
        if type(int(line[0]))==int:
            print(line)
            file.write(str(parse_rpn(line))+"\n")
            tn.write(str(parse_rpn(line))+"\n")
            print(parse_rpn(line))

    except ValueError:
        print(line)
        continue
