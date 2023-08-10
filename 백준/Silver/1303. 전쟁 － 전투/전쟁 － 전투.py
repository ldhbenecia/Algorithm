from collections import deque

def bfs(x, y, color):
  visited[x][y] = True
  
  queue = deque()
  queue.append((x, y))
  cnt = 0
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if (0 <= nx < m and 0 <= ny < n):
        if graph[nx][ny] == color and visited[nx][ny] == False:
          visited[nx][ny] = True
          cnt += 1
          queue.append((nx, ny))
          
  return cnt + 1
    
  
  
n, m = map(int, input().split())

graph = [list(input()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
  
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

whiteCount = 0
blueCount = 0

for i in range(m):
  for j in range(n):
    if graph[i][j] == "W" and not visited[i][j]:
      whiteCount += bfs(i, j, "W") ** 2
    elif graph[i][j] == "B" and not visited[i][j]:
      blueCount += bfs(i, j, "B") ** 2

print(whiteCount, blueCount)
