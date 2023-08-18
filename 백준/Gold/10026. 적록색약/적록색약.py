import sys
sys.setrecursionlimit(10000)

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False] * (n) for _ in range(n)]

original = 0
colorWeakness = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

    
def dfs(x, y):
  visited[x][y] = True
  currentColor = graph[x][y]
  
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    
    if (0 <= nx < n) and (0 <= ny < n):
      if visited[nx][ny] == False:
        if graph[nx][ny] == currentColor:
          dfs(nx, ny)
        
# 적록색약이 아닐 경우 (original)
for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      dfs(i, j)
      original += 1
      
# 적록색약일 경우 (R -> G)
for i in range(n):
  for j in range(n):
    if graph[i][j] == 'R':
      graph[i][j] = 'G'
      
# 새로 세야됨 -> 초기화
visited = [[False] * (n) for _ in range(n)] 
  
for i in range(n):
  for j in range(n):
    if visited[i][j] == False:
      dfs(i, j)
      colorWeakness += 1
      
print(original, colorWeakness)
