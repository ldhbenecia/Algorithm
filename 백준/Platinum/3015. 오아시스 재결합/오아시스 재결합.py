n = int(input())
line = [int(input()) for _ in range(n)]

stack = []
result = 0

for i in line:
  # 스택 마지막 값보다 키가 클 경우
  while stack and stack[-1][0] < i:
    result += stack.pop()[1]
    
  # 스택이 비어있을 경우
  if not stack:
    stack.append((i, 1))
  else:
    # 스택 마지막 값과 키가 같을 경우
    if stack[-1][0] == i:
      cnt = stack.pop()[1]
      result += cnt
      
      if stack: result += 1
      stack.append((i, cnt + 1))
    # 스택 마지막 값보다 작을 경우
    else:
      stack.append((i, 1))
      result += 1
  
print(result)
  