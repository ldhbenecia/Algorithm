from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

# 익은 토마토 위치 삽입
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      queue.append([i, j])

# 최소 일수를 구하는 것 -> BFS로 풀이
def bfs():
  while queue:
    x, y = queue.popleft() # 익은 토마토 위치
    
    # 상하좌우 탐색
    for i in range(4):
      nx, ny = dx[i] + x, dy[i] + y
      # 그래프 범위 안이고 익지 않은 경우 (0)
      if 0 <= nx < n and 0 <= ny < m :
        if graph[nx][ny] == 0:
          graph[nx][ny] = graph[x][y] + 1 # 익힘 전염 +1 
          queue.append([nx, ny])
  
bfs()

flag = True
for i in graph:
  for j in i:
    if j == 0:
      flag = False
    
  result = max(result, max(i))

if flag == False:
  print(-1)
else:
  print(result - 1)
