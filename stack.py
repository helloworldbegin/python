class Stack():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def push(self,value):
        self.items.append(value)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

def parChk(symbol_string):
    stack=Stack()
    balanced=True
    for i in symbol_string:
        if i == "(":
            stack.push(i)
        else:
            if stack.isEmpty():
                balanced=False
            else:
                stack.pop()
    if stack.isEmpty() and balanced:
        return True
    else:
        return False
    
def parCheck(symbol_string):
    stack=Stack()
    balanced=True
    for i in symbol_string:
        if i in '([{':
            stack.push(i)
        else:
            if stack.isEmpty():
                balanced=False
            else:
                top=stack.pop()
                if matches(top,i):
                    continue
                else:
                    balanced=False
    if stack.isEmpty() and balanced:
        return True
    else:
        return False
    
def matches(open,close):
    op='([{'
    cl=')]}'
    return op.index(open) == cl.index(close)

def decimalToBinary(decimal_number):
    stack=Stack()

    while decimal_number > 0:
        stack.push(decimal_number % 2)
        decimal_number = decimal_number // 2

    string = ""

    while not stack.isEmpty():
        string = string + str(stack.pop())

    return string

def decimalToEight(decimal_number):
    stack=Stack()

    while decimal_number > 0:
        stack.push(decimal_number % 8)
        decimal_number = decimal_number // 8

    string = ""

    while not stack.isEmpty():
        string = string + str(stack.pop())

    return string

def decimalToHex(decimal_number):
    stack=Stack()

    while decimal_number > 0:
        stack.push(decimal_number % 16)
        decimal_number = decimal_number // 16

    string = ""

    while not stack.isEmpty():
        decimal=[10,11,12,13,14,15]
        hexnum=['A','B','C','C','E','F']
        string = string + (str(stack.pop()) if stack.peek() <= 9 else \
                           hexnum[decimal.index(stack.pop())])

    return string


def baseConverter(decimal_number, base):
    digits="0123456789ABCDEF"

    stack=Stack()

    while decimal_number > 0:
        stack.push(decimal_number % base)
        decimal_number decimal_number // base

    string = ""
    while not stack.isEmpty():
        string = string + digits[stack.pop()]
    return string
