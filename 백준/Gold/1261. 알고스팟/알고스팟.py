import sys
from collections import deque
input = sys.stdin.readline

def bfs():
  queue = deque([(0, 0)])
  visited[0][0] = 0
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      
      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
        if graph[nx][ny] == 0: # 빈 방 (가중치 0)
          visited[nx][ny] = visited[x][y]
          queue.appendleft((nx, ny)) # 빈 방인경우 우선적으로 방문 (안 부실 수 있음)
        else: # 벽 (가중치 1)
          visited[nx][ny] = visited[x][y]+1
          queue.append((nx, ny))
          
  return visited[n - 1][m - 1]
          
m, n = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())