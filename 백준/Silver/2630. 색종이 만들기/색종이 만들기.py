import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

def solution(n, x, y):
  global white, blue
  
  half = n // 2
  color = graph[x][y]
  
  for i in range(x, x + n):
    for j in range(y, y + n):
      if graph[i][j] != color:
        solution(half, x, y)
        solution(half, x + half, y)
        solution(half, x, y + half)
        solution(half, x + half, y + half)
        return
        
  if color == 0:
    white += 1
  else:
    blue += 1
      
solution(n, 0, 0)
print(white)
print(blue)