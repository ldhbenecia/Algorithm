from collections import deque

R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

fire_time = [[-1] * C for _ in range(R)]
jihun_time = [[-1] * C for _ in range(R)]

fire_q = deque()
jihun_q = deque()

for i in range(R):
    for j in range(C):
        if graph[i][j] == "F":
            fire_q.append((i, j))
            fire_time[i][j] = 0
        elif graph[i][j] == "J":
            jihun_q.append((i, j))
            jihun_time[i][j] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while fire_q:
    x, y = fire_q.popleft()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] != "#" and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_q.append((nx, ny))

while jihun_q:
    x, y = jihun_q.popleft()

    # base
    if x == 0 or x == R - 1 or y == 0 or y == C - 1:
        print(jihun_time[x][y] + 1)
        exit()

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < R and 0 <= ny < C:
            if graph[nx][ny] != "#" and jihun_time[nx][ny] == -1:
                # 불보다 먼저 도착하거나, 이동을 해도 불이 없는 곳
                if fire_time[nx][ny] == -1 or jihun_time[x][y] + 1 < fire_time[nx][ny]:
                    jihun_time[nx][ny] = jihun_time[x][y] + 1
                    jihun_q.append((nx, ny))

print("IMPOSSIBLE")
