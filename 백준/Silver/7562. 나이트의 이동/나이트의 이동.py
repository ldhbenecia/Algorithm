from collections import deque

t = int(input())

dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, -2, -1, 1, 2]

def bfs():
  queue = deque()
  queue.append((cx, cy))
  
  while queue:
    x, y = queue.popleft()
    
    if x == mx and y == my:
      return graph[mx][my]
    
    for i in range(8):
      nx = dx[i] + x
      ny = dy[i] + y
      
      if (0 <= nx < l and 0 <= ny < l):
        if graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y] + 1 # cnt += 1
          queue.append((nx, ny))
  
for _ in range(t):
  l = int(input()) # 체스판의 한 변의 길이, 체스판의 크기는 l * l
  cx, cy = map(int, input().split()) # 현재 위치
  mx, my = map(int ,input().split()) # 이동할 위치
  graph = [[0] * l for _ in range(l)]
  graph[cx][cy] = 0 # cnt
  print(bfs())