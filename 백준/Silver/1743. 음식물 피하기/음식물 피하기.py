from collections import deque

def bfs(x, y):
  global count
  queue = deque([(x, y)])
  
  graph[x][y] = 0
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
        count += 1
        
  return count

n, m, k = map(int, input().split())
graph = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
  r, c = map(int, input().split())
  graph[r - 1][c - 1] = 1 # 음식물 쓰레기

max_size = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      count = 1
      max_size = max(bfs(i, j), max_size)
      
print(max_size)
