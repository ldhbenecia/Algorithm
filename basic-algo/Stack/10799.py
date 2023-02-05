n = list(input())
stack = []
cnt = 0

for i in range(len(n)):
  
  if n[i] == "(":
    stack.append(i)
    
  else: # ")" 나왔을 때
    if n[i-1] == "(": # ()라면
      stack.pop()
      cnt += len(stack)
    else:
      stack.pop()
      cnt += 1
      
print(cnt)