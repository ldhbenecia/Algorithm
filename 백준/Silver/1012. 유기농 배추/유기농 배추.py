import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
    
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    
    if (0 <= nx < n and 0 <= ny < m):
      if graph[nx][ny] == 1:
        graph[nx][ny] = -1
        dfs(nx, ny)
          
          
t = int(input())

for _ in range(t):
  m, n, k = map(int, input().split())
  graph = [[0] * m for _ in range(n)]
  cnt = 0
  
  for _ in range(k):
    x, y = map(int, input().split())
    graph[y][x] = 1 # 이 문제는 행렬이 아닌 x, y 좌표계로 입력함
    
  for i in range(n):
    for j in range(m):
      if graph[i][j] > 0:
        dfs(i, j)
        cnt += 1

  print(cnt)