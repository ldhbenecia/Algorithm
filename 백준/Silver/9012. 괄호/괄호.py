t = int(input())

for _ in range(t):
    bucket = input()

    stack = []
    for i in bucket:
        if i == "(":
            stack.append(i)
        if i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")

    if not stack:
        print("YES")
    else:
        print("NO")
