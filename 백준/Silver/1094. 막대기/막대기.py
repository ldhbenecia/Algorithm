x = int(input())

result = 0
default = 64

while x > 0:
    if default > x:
        default //= 2
    else:
        result += 1
        x -= default

print(result)
