from collections import deque

def bfs():
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
        
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        return -1
      
  max_day = max(max(row) for row in graph)
  return max_day - 1
  
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([])

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      queue.append((i, j))

        
# 모든 토마토가 익었을 때의 일수 출력
print(bfs())