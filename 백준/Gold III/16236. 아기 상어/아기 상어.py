from collections import deque

def bfs():
  queue = deque([(now_i, now_j)])
  distance = [[-1] * n for _ in range(n)]
  distance[now_i][now_j] = 0
  
  while queue:
    x, y = queue.popleft()
        
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      
      if 0 <= nx < n and 0 <= ny < n:
        if shark_size >= graph[nx][ny] and distance[nx][ny] == -1:
          distance[nx][ny] = distance[x][y] + 1
          queue.append((nx, ny))

  return distance

def bite(distance):
    min_distance = 1e9
    min_x, min_y = 0, 0
    
    for i in range(n):
      for j in range(n):
        if distance[i][j] != -1 and 1 <= graph[i][j] < shark_size:
          if distance[i][j] < min_distance:
            min_x, min_y = i, j
            min_distance = distance[i][j]
        
    # 먹을 물고기가 없을 경우 min_distance 값이 변화 x            
    if min_distance == 1e9:
        return None
    else:
        return min_x, min_y, min_distance
      
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
now_i, now_j = 0, 0
shark_size = 2

# 현재 상어 좌표
for i in range(n):
  for j in range(n):
    if graph[i][j] == 9:
      now_i, now_j = i, j
      graph[i][j] = 0
      
time = 0
ate_fish = 0
while True:
  result = bite(bfs())
  if result is None:
    break
  else:
    x, y, distance = result
    now_i, now_j = x, y
    graph[now_i][now_j] = 0
    ate_fish += 1
    if ate_fish == shark_size:
      shark_size += 1
      ate_fish = 0
    time += distance

print(time)