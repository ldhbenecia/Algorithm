n = int(input())

cnt = 1
stack = []
answer = []
temp = True

for _ in range(n):
  x = int(input())
  
  while cnt <= x: # 처음 시작하는 값까지는 push
    stack.append(cnt)
    answer.append("+")
    cnt += 1
    
  if stack[-1] == x: # 예제처럼 4가 처음 나왔을 시
    stack.pop()
    answer.append("-")
  else:
    temp = False
    break
    
if temp == False:
  print("NO")

else:
  for i in answer:
    print(i)