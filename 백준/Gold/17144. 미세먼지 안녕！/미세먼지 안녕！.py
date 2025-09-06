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


def operate_air_cleaner():
    up, down = purifier

    # 위쪽 (반시계)
    for i in range(up - 1, 0, -1):  # 세로
        graph[i][0] = graph[i - 1][0]
    for j in range(c - 1):  # 가로
        graph[0][j] = graph[0][j + 1]
    for i in range(up):  # 세로
        graph[i][c - 1] = graph[i + 1][c - 1]
    for j in range(c - 1, 1, -1):  # 가로
        graph[up][j] = graph[up][j - 1]
    graph[up][1] = 0  # 청정기 바로 옆

    # 아래쪽 (시계)
    for i in range(down + 1, r - 1):  # 4 6
        graph[i][0] = graph[i + 1][0]
    for j in range(c - 1):  # 0 ~ 7
        graph[r - 1][j] = graph[r - 1][j + 1]
    for i in range(r - 1, down, -1):  # 6 ~ 3
        graph[i][c - 1] = graph[i - 1][c - 1]
    for j in range(c - 1, 1, -1):
        graph[down][j] = graph[down][j - 1]
    graph[down][1] = 0  # 청정기 바로 옆

    graph[up][0] = -1
    graph[down][0] = -1


r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

purifier = []  # 공기청정기 위치
for i in range(r):
    if graph[i][0] == -1:  # 1열메만 존재하므로
        purifier.append(i)

for _ in range(t):
    graph = diffusion()  # 미세먼지 확산
    operate_air_cleaner()  # 공기청정기 실행

result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)
