def solution(s):
    answer = True
    stack = []
    
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        if s[i] == ")":
            if "(" in stack:
                stack.pop()
            else:
                answer = False
                
    if "(" in stack:
        answer = False
    if ")" in stack:
        answer = False

    return answer
