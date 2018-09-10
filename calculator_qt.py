def isEmpty(self):
    return len(self) == 0

def peek(self):
    if not isEmpty(self):
        return self[-1]

def SimpleCalculate(firstnumstr, symbol, secondnumstr):
    firstnum = float(firstnumstr)
    secondnum = float(secondnumstr)
    if(symbol == '+'):
        return (firstnum + secondnum)
    elif(symbol == '-'):
        return (firstnum - secondnum)
    elif(symbol == '*'):
        return (firstnum * secondnum)
    elif(symbol == '/'):
        return (firstnum / secondnum)
    else:
        print('SimpleCalculate_error')


expstring = input('Input your expression: ')
print(expstring)
str = ""
a = []
b = []

for item in expstring:
    if(item != '+' and item != '-' and item != '*' and item != '/'):
        str += item
    else:
        if(item == '+' or item == '-'):
            while(True):
                if(peek(b) == '+' or peek(b) == '-'):
                    b.append(item)
                    a.append(float(str))
                    str = ""
                    print(a)
                    print(b)
                    print('(1)')
                    break
                elif(isEmpty(b) and isEmpty(a)):
                    b.append(item)
                    a.append(float(str))
                    str = ""
                    print(a)
                    print(b)
                    print('(2)')
                    break
                else:
                    p = a.pop()
                    q = b.pop()
                    print(p, q, str)
                    str = SimpleCalculate(p, q, str)
                    print(str)
                    print('(3)')

        elif(item == '*' or item == '/'):
            b.append(item)
            a.append(float(str))
            print(a)
            print(b)
            print('(4)')
            str = ""

        print('(5)')

while(len(b) or len(a)):
    x, y = a.pop(), b.pop()
    print(x, y, str)
    str = SimpleCalculate(x, y, str)
    print(str)
    print('(6)')