from collections import deque

def bfs(X, Y):
  queue = deque(virus)
  
  while queue:
    kind, time, x, y = queue.popleft()
    
    # 종료조건: 시간이 s가 되면 종료
    if time == S:
      break
    
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      
      if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 0:
        graph[nx][ny] = kind
        queue.append((kind, time + 1, nx, ny))
        
  return graph[X - 1][Y - 1]


n, k = map(int, input().split())
graph = []
virus = []

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(n):
    if graph[i][j] != 0:
      virus.append((graph[i][j], 0, i, j))

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

virus.sort()
print(bfs(X, Y))
