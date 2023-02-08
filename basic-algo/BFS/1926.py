from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]  # 동 서 남 북
dy = [0, 0, -1, 1]

cnt = 0
max_area = 0

def BFS(x, y):
  q = deque()
  w = 1 # 최초 크기 설정, 1로 초기화를 계속 해주지 않으면 값이 누적됨
  
  # 초기 세팅
  visited[x][y] = True
  q.append([x, y])
  
  while q: # queue에 남은 것이 없을 때까지 반복
    x, y = q.popleft() # queue에 가장 먼저 들어온 원소 빼기
    
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      if 0 <= nx < n and 0 <= ny < m: # 범위 안에 있는 지
        if grid[nx][ny] == 1 and not visited[nx][ny]: # 그림이 있는 지(1인지), 방문을 안한 곳인지
          visited[nx][ny] = True # 방문했다고 체크
          q.append([nx, ny])
          w += 1
  return w

for i in range(n):
  for j in range(m):
    if grid[i][j] == 1 and not visited[i][j]: # 그림이 있고 방문을 안한 곳인지
      cnt += 1
      max_area = max(max_area, BFS(i, j)) # 0으로 초기화되어있는 max_area가 BFS를 돌면서 계속 업데이트 됨
      
print(cnt)
print(max_area)