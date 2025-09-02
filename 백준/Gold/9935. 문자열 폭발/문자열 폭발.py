st = input()
boom = input()

stack = []
for i in st:
    stack.append(i)

    if len(stack) >= len(boom):
        if "".join(stack[-len(boom) :]) == boom:
            for _ in range(len(boom)):
                stack.pop()

result = "".join(stack)

if result:
    print(result)
else:
    print("FRULA")
