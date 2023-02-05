n = int(input())
cnt = 0

for _ in range(n):
  word = input()
  stack = []
  
  for i in word:
    if not stack:
      stack.append(i)
    else:
      if stack[-1] == i:
        stack.pop()
      else:
        stack.append(i)
        
  if len(stack) == 0:
    cnt += 1
    
print(cnt)