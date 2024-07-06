s = input()

result = 0
stack = []

temp = 1
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        temp *= 2

    elif s[i] == '[':
        stack.append(s[i])
        temp *= 3

    elif s[i] == ')': 
        # 올바른 괄호열 판별
        if not stack or stack[-1] == '[':
            result = 0
            break
        if s[i - 1] == '(':
            result += temp
        stack.pop()
        temp //= 2

    elif s[i] == "]":
        # 올바른 괄호열 판별
        if not stack or stack[-1] == "(":
            result = 0
            break
        if s[i - 1] == "[":
            result += temp
        stack.pop()
        temp //= 3
        
if not stack:
    print(result)
else:
    print(0)
