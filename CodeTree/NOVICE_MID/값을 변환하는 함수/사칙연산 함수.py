a, o, c = input().split()
a = int(a)
c = int(c)

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b
    
def divide(a, b):
    return a // b

if o == '+':
    print(a, "+", c, "=", plus(a, c))
elif o == '-':
    print(a, "-", c, "=", minus(a, c))
elif o == '*':
    print(a, "*", c, "=", times(a, c))
elif o == '/':
    print(a, "/", c, "=", divide(a, c))
else:
    print("False")