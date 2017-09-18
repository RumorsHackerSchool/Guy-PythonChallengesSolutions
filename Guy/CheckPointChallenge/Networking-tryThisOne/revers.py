
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

expression = raw_input("Please type RPM: ")
print(type(expression))
print (parse_rpn(expression))