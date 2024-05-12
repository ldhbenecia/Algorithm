from collections import deque
import copy

# 벽 만들기
def make_wall(count):
  if count == 3: # 벽 3개 다 지었으면 안전영역 크기 재기
    bfs()
    return
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        make_wall(count + 1)
        graph[i][j] = 0
        
  
# 안전영역 크기 재기
def bfs():
  queue = deque()
  test = copy.deepcopy(graph)
  
  for i in range(n):
    for j in range(m):
      if test[i][j] == 2:
        queue.append((i, j))
  
  # 바이러스 전염 시작
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      
      if 0 <= nx < n and 0 <= ny < m:
        if test[nx][ny] == 0:
          test[nx][ny] = 2 # 바이러스 전염
          queue.append((nx, ny))
  
  global result
  count = 0
  for i in range(n):
    for j in range(m):
      if test[i][j] == 0:
        count += 1
  
  result = max(result, count)
  
  
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
make_wall(0)

print(result)


'''
벽을 짓는 함수, 안전영역 크기를 재는 함수(BFS) 생성
-----
빈 칸 (0인 경우)에 대해 벽을 쌓기 시작
count == 3이 되면 bfs 탐색해서 바이러스 전염 후 안전영역 크기 카운팅

안전 영역 크기 중 가장 큰 값 도출
'''