N = int(input())
buildings = [int(input()) for _ in range(N)]

stack = []
result = 0

for cur in buildings:
    while stack and stack[-1] <= cur:
        stack.pop()

    result += len(stack)
    stack.append(cur)

print(result)
