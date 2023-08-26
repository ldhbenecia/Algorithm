import sys
sys.setrecursionlimit(15000)

def dfs(x, y, height):
  visited[x][y] = True
  
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    
    if 0 <= nx < n and 0 <= ny < n:
      if not visited[nx][ny] and graph[nx][ny] > height:
        dfs(nx, ny, height)

n = int(input())
graph = [list(map(int ,input().split())) for _ in range(n)]
max_height = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  for j in range(n):
    if graph[i][j] > max_height:
      max_height = graph[i][j]

max_safe_area = 0
for height in range(max_height + 1):
  visited = [[False] * (n) for _ in range(n)]
  safe_area = 0
  for i in range(n):
    for j in range(n):
      if not visited[i][j] and graph[i][j] > height:
        dfs(i, j, height)
        safe_area += 1
  max_safe_area = max(max_safe_area, safe_area)  
    
print(max_safe_area)