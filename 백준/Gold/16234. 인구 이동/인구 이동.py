import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
  queue = deque([(x, y)])
  union = [(x, y)]
  
  visited[x][y] = True
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
        if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
          visited[nx][ny] = True
          queue.append((nx, ny))
          union.append((nx, ny))

  return union

N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

day = 0
while True:
  visited = [[False] * (N) for _ in range(N)]
  move = False
  
  for i in range(N):
    for j in range(N):
      if not visited[i][j]:
        union = bfs(i, j) # 연합 x, y좌표
        
        # 인구 이동
        if len(union) > 1:
          move = True
          # union으로 받은 x, y 좌표를 통한 인구 총합 계산
          population = sum(graph[i][j] for i, j in union) // len(union)
          
          # 연합국들은 연합 인구로 최신화
          for x, y, in union:
            graph[x][y] = population
            
  if move == False:
    break
  
  day += 1

print(day)