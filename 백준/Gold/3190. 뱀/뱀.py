from collections import deque

# L은 오른쪽, D는 오른쪽 90도 회전
def turn(direction, c):
  if c == 'L':
    direction = (direction - 1) % 4
  else:
    direction = (direction + 1) % 4
    
  return direction

def simulate():
  x, y = 1, 1 # 뱀 초기 위치 값
  graph[x][y] = 8 # 뱀이 위치하는 곳은 8로 설정
  direction = 1 # 내가 짠 dx, dy에서 동쪽의 인덱스는 1임
  time = 0
  
  queue = deque([(x, y)]) # 뱀 위치
  while True:
    # 초기 동쪽 세팅 (뱀은 처음에 오른쪽을 향한다)
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 종료조건: 벽에 부딪히거나 자기 자신에게 닿으면 종료
    if not (1 <= nx <= n and 1 <= ny <= n) or graph[nx][ny] == 8:
      time += 1
      break
    
    # 사과가 없다면
    if graph[nx][ny] == 0:
      # 이동
      graph[nx][ny] = 8
      queue.append((nx, ny))
      # 이동 후 이동 전 위치 삭제
      prev_x, prev_y = queue.popleft()
      graph[prev_x][prev_y] = 0
      
    # 사과가 있다면
    elif graph[nx][ny] == 1:
      graph[nx][ny] = 8
      queue.append((nx, ny))
      
    # 이동 이후 최신화
    x, y = nx, ny
    time += 1
    
    # 방향 전환
    if time in direction_info:
      direction = turn(direction, direction_info[time])
      
  return time
    

n = int(input())
k = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
direction_info = {}

# 보드에 사과 등록
for _ in range(k):
  col, row = map(int, input().split())
  graph[col][row] = 1

# 방향 회전 정보 등록
l = int(input())
for _ in range(l):
  x, c = input().split()
  direction_info[int(x)] = c

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(simulate())
