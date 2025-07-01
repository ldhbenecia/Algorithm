while True:
    s = input()
    if s == ".":
        break

    stack = []
    is_valid = True

    for i in s:
        if i == "(" or i == "[":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                is_valid = False
                break
        elif i == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                is_valid = False
                break

    if not stack and is_valid:
        print("yes")
    else:
        print("no")
