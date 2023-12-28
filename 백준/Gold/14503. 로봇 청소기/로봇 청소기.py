n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

count = 0

dx = [-1, 0, 1, 0]  # 북 동 남 서
dy = [0, 1, 0, -1]  # 북 동 남 서

# 로봇 청소기 배정된 칸이 0인 경우
if (graph[r][c] == 0):
  graph[r][c] = -1
  count += 1

while True:
  for _ in range(4):
    # 반시계 공식
    d = (d + 3) % 4
    nx, ny = r + dx[d], c + dy[d]
    
    # 왼쪽 방향에 아직 청소하지 않은 공간이 있다면
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
      graph[nx][ny] = -1  # 청소
      count += 1
      r, c = nx, ny
      break

  # 네 방향 모두 청소가 이미 되어 있거나 벽인 경우
  else:
    # 후진 공식
    back_d = (d + 2) % 4
    nx, ny = r + dx[back_d], c + dy[back_d]

    # 뒤쪽 방향이 벽이 아니면 후진
    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
      r, c = nx, ny
    else:
      break

print(count)
