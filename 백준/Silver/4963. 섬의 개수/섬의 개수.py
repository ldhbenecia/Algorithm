from collections import deque

def bfs(x, y):
  queue = deque([(x, y)])
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(8):
      nx = dx[i] + x
      ny = dy[i] + y
      
      if 0 <= nx < h and 0 <= ny < w:
        if graph[nx][ny] == 1:
          graph[nx][ny] = 0
          queue.append((nx, ny))

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, 1, -1, 1, -1]

while True:
  w, h = map(int, input().split())
  
  if w == 0 and h == 0:
    break

  graph = []
  answer = 0
  
  for i in range(h):
    maps = list(map(int, input().split()))
    graph.append(maps)
    
  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        bfs(i, j)
        answer += 1

  print(answer)