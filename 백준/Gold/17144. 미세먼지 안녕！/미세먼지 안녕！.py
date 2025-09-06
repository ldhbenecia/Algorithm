def diffusion():
    # 확산 결과를 저장할 임시 배열
    temp = [[0] * c for _ in range(r)]

    # 공기 청정기 위치는 -1로 유지
    for i in range(r):
        for j in range(c):
            if graph[i][j] != -1 and graph[i][j] != 0:
                spread = graph[i][j] // 5
                cnt = 0

                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        temp[nx][ny] += spread
                        cnt += 1
                # 주변은 // 5 값을 넣고 시작점 연산: 확산하고 남은 값 연산
                temp[i][j] += graph[i][j] - spread * cnt
            elif graph[i][j] == -1:
                temp[i][j] = -1
    return temp


def clean_up():
    x, y = purifier[0][0], purifier[0][1] + 1  # 시작 좌표, 공기청정기 다음 위치 값 부터
    direction = 0  # 동쪽으로 시작
    prev = 0

    while True:
        nx = dx[direction] + x
        ny = dy[direction] + y

        # 모서리 도착 시 시계방향으로 회전
        if nx == r or ny == c or nx == -1 or ny == -1:
            direction = (direction - 1) % 4
            continue

        # 공기청전기 부위에 도착시 중단 조건 (base)
        if x == purifier[0][0] and y == purifier[0][1]:
            break

        graph[x][y], prev = prev, graph[x][y]
        x, y = nx, ny


def clean_down():
    x, y = purifier[1][0], purifier[1][1] + 1  # 시작 좌표, 공기청정기 다음 위치 값 부터
    direction = 0  # 동쪽으로 시작
    prev = 0

    while True:
        nx = dx[direction] + x
        ny = dy[direction] + y

        # 모서리 도착 시 시계방향으로 회전
        if nx == r or ny == c or nx == -1 or ny == -1:
            direction = (direction + 1) % 4
            continue

        # 공기청전기 부위에 도착시 중단 조건 (base)
        if x == purifier[1][0] and y == purifier[1][1]:
            break

        graph[x][y], prev = prev, graph[x][y]
        x, y = nx, ny


r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

purifier = []  # 공기청정기 위치
for i in range(r):
    for j in range(c):
        if graph[i][j] == -1:  # 1열메만 존재하므로
            purifier.append((i, j))

# t초 동안 한번에 확산 후 공기청정기 실행
for _ in range(t):
    graph = diffusion()
    clean_up()
    clean_down()

result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)
