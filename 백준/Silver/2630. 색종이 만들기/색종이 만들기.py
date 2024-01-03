n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0

def dfs(x, y, n):
  global white, blue;
  half_size = n // 2
  color = graph[x][y]
  
  for i in range(x, x + n):
    for j in range(y, y + n):
      if color != graph[i][j]:
        dfs(x, y, half_size) # 2사분면
        dfs(x, y + half_size, half_size) # 1사분면
        dfs(x + half_size, y, half_size) # 3사분면
        dfs(x + half_size, y + half_size, half_size) # 4사분면
        return
  
  if color == 0:
    white += 1
  else:
    blue += 1
  
dfs(0, 0, n)
print(white)
print(blue)