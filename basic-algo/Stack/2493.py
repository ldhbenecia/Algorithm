n = int(input())
topList = list(map(int, input().split()))
stack = []
answer = []

for i in range(n):
  while stack: # stack에 값이 여러개 남아있으면 거기까지 반복해서 돌려야하므로
    if stack[-1][0] > topList[i]: 
      answer.append(stack[-1][1] + 1)
      break
    else:
      stack.pop()

  if not stack:
    answer.append(0)
  stack.append([topList[i], i])
  
print(" ".join(map(str, answer)))