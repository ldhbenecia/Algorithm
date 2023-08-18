n = int(input())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * (n) for _ in range(n)]

cnt = 0 # 각 단지내 집 수
result = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
  global cnt
  visited[x][y] = True
  cnt += 1
  
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    
    if (0 <= nx < n and 0 <= ny < n):
      if visited[nx][ny] == False:
        if graph[nx][ny] == 1:
          visited[nx][ny] = True
          dfs(nx, ny)

  return cnt

result = []

for i in range(n):
  for j in range(n):
    if graph[i][j] == 1 and visited[i][j] == False:
      result.append(dfs(i, j))
      cnt = 0

result.sort()

print(len(result))
for i in result:
  print(i)
