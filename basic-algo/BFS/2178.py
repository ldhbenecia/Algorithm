from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]  # 동 서 남 북
dy = [0, 0, -1, 1]

# (1, 1)부터라고 하지만 (0, 0)으로 잡음
# BFS를 이용하여 동 서 남 북을 검사하여 이동하였을 때 1인 값을 찾음 (값이 1이면 이동)
# 만약 1이라면 그 전 값에 +1을 하여 이동할 때 지나야 하는 최소 칸 수를 더해 줌
# 그러면 예시의 4,6칸에는 +1씩 더해져 15가 들어가있을 것임

# 이 외의 방법으로는 1인 방향을 찾아갔을때 그 값들을 따로 리스트를 만들어
# 이전 그림문제처럼 visited 리스트가 아니라 다른 리스트 하나 만들어서 그 리스트의 sum을 해도 될 것 같음
def BFS(x, y):
  q = deque()
  q.append([x, y])
  
  while q:
    x, y = q.popleft() # queue에 가장 먼저 들어온 원소 빼기
    
    for i in range(4): # 4가지 방향으로 위치 확인
      nx = dx[i] + x
      ny = dy[i] + y
      if 0 <= nx < n and 0 <= ny < m: # 범위 안에 있는 지
        if grid[nx][ny] == 1:
          q.append([nx, ny])
          grid[nx][ny] = grid[x][y] + 1
  return grid[n-1][m-1] # 0, 0부터 우리는 시작하므로 -1씩 해주기

print(BFS(0, 0))