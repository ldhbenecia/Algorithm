n = int(input())
h = [int(input()) for _ in range(n)]

stack = []
answer = 0

for i in range(n):
  while stack and stack[-1] <= h[i]: # stack이 비어있지 않고 stack 이전 값이 현재 빌딩보다 낮을 때
    stack.pop()
  stack.append(h[i])
  answer += len(stack) - 1 # -1을 하는 이유는 현재 빌딩은 제외해야하므로
  
print(answer)