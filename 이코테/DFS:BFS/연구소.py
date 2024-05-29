import copy
from collections import deque

# 벽 3개 세우기
def make_wall(count):
  # 벽이 3개 세워지면 바이러스 전염 시킨 후 안전영역 크기 재기
  if count == 3:
    bfs()
    return
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        make_wall(count + 1)
        graph[i][j] = 0

def bfs():
  queue = deque()
  # 현재 벽이 3개 세워진 그래프 상태 복사
  current_graph = copy.deepcopy(graph)
  
  # 바이러스 위치 탐색
  for i in range(n):
    for j in range(m):
      if current_graph[i][j] == 2:
        queue.append((i, j))
  
  # 바이러스 전염 시작
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      
      if 0 <= nx < n and 0 <= ny < m and current_graph[nx][ny] == 0:
        current_graph[nx][ny] = 2
        queue.append((nx, ny))
        
  # 전염이 끝난 이후 안전영역 개수 세기
  global save_space
  count = 0
  for i in range(n):
    for j in range(m):
      if current_graph[i][j] == 0:
        count += 1
        
  save_space = max(save_space, count)

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

save_space = 0
make_wall(0)

print(save_space)

# 1. 완전 탐색으로 벽 3개를 설치
# 1-1. 벽 3개가 설치 되면 바이러스가 전부 퍼지게 하기
# 2. 안전영역의 개수 구하기