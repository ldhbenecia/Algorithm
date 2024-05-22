import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, z):
  queue = deque([(x, y, z)])
  building[x][y][z] = 1 # 방문표시와 함께 minute 세기
  
  while queue:
    x, y, z = queue.popleft()
    
    for i in range(6):
      nx = dx[i] + x
      ny = dy[i] + y
      nz = dz[i] + z
      
      if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
        if building[nx][ny][nz] == '.':
          building[nx][ny][nz] = building[x][y][z] + 1
          queue.append((nx, ny, nz))
        elif building[nx][ny][nz] == 'E':
          return building[x][y][z]
          
  return 'Trapped!'

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:
  L, R, C = map(int, input().split())
  
  if L == 0 and R == 0 and C == 0:
    break
  
  building = []
  for _ in range(L):
    building.append([list(input().strip()) for _ in range(R)])
    input()
    
  for i in range(L):
    for j in range(R):
      for k in range(C):
        if building[i][j][k] == 'S':
          result = bfs(i, j, k)
          if result == 'Trapped!':
            print("Trapped!")
          else:
            print(f"Escaped in {result} minute(s).")