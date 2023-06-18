n, m = map(int,input().split())
x, y, dir = map(int,input().split()) # 캐릭터 위치 좌표, 방향

grid = [[0] * m for _ in range(n)] # 지도 0으로 초기화, 가본 위치는 1로 표시할 것이기 때문
grid[x][y] = 1 # 캐릭터 시작 지점 방문 체크

# 지도 육지, 바다 설정
array = []
for i in range(n):
  array.append(list(map(int,input().split())))

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = [0, 1, 2, 3] # 북 동 남 서

# 왼쪽 방향으로 회전
def turn_left():
  global dir
  dir -= 1
  if dir == -1: # 북쪽에서 회전할 경우
    dir = 3 # 서쪽

# 시뮬레이션 시작
count = 1 # 방문한 칸 개수 카운트
block = 0 # 못 가는 방향 개수

while True:
  turn_left() # 왼쪽으로 회전
  nx = x + dx[dir] # 현재 위치에서 바라보는 방향으로 이동
  ny = y + dy[dir] # 현재 위치에서 바라보는 방향으로 이동
  
  # 그 칸이 안가봤고 (0), 육지라면 전진
  if grid[nx][ny] == 0 and array[nx][ny] == 0:
    grid[nx][ny] = 1
    count += 1
    x = nx # 이동
    y = ny # 이동
    block = 0
    continue # 계속 진행
  else: # 가본 칸이거나, 바다일 경우
    block += 1
    
  # 네 방향 모두 이미 가봤거나, 바다인 경우
  if block == 4: # 사방이 못감
    nx = x - dx[dir]
    ny = y - dy[dir]
    
    if array[nx][ny] == 0: # 뒤쪽이 육지인 경우, 이미 가본 곳으로 왔으니 count 증가 안함
      x = nx
      y = ny
    else: # 뒤쪽이 바다인 경우
      break  # 정지, 종료
    
    block = 0
    
print(count)