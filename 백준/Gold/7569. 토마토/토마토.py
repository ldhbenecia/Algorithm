from collections import deque

def bfs():
  while queue:
    x, y, z = queue.popleft()
    
    for i in range(6):
      nx = dx[i] + x
      ny = dy[i] + y
      nz = dz[i] + z
      
      if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and graph[nx][ny][nz] == 0:
        graph[nx][ny][nz] = graph[x][y][z] + 1
        queue.append((nx, ny, nz))
        
  for i in range(h):
    for j in range(n):
      for k in range(m):
        if graph[i][j][k] == 0:
          return -1
      
  max_day = max(max(max(row) for row in graph[i]) for i in range(h))
  return max_day - 1

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque([])

for i in range(h):
  for j in range(n):
    for k in range(m):
      if graph[i][j][k] == 1:
        queue.append((i, j, k))

# 모든 토마토가 익었을 때의 일수 출력
print(bfs())
