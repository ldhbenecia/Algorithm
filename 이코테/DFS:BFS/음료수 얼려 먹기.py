def dfs(x, y):
  graph[x][y] = -1
  
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    
    if (0 <= nx < n) and (0 <= ny < m):
      if graph[nx][ny] == 0:
        graph[nx][ny] = -1
        dfs(nx, ny)
  

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      dfs(i, j)
      cnt += 1

print(cnt)
  

'''
4 5
00110
00011
11111
00000
'''
# 정답: 3

'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''
# 정답: 8