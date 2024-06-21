from collections import deque

def is_valid(s):
    stack = []
    for char in s:
        if char in "({[":
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if char == ')' and top != '(':
                return False
            if char == '}' and top != '{':
                return False
            if char == ']' and top != '[':
                return False
    return not stack

def solution(s):
    answer = 0
    s = deque(s)
    
    for _ in range(len(s)):
        if is_valid(s):
            answer += 1
        s.rotate(-1)
        
    return answer