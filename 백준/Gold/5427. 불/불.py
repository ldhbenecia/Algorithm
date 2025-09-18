from collections import deque


# 불의 확산을 처리해서 불 도착 시간을 기록
def fire_bfs(fire):
    fire_time = [[-1] * w for _ in range(h)]

    queue = deque()
    for x, y in fire:
        queue.append((x, y))
        fire_time[x][y] = 0  # 불 위치 0으로 초기화 (이미 처음부터 나고 있으니까)

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < h and 0 <= ny < w:
                if (
                    graph[nx][ny] != "#" and fire_time[nx][ny] == -1
                ):  # 확산한 적이 없는 곳이어야함
                    queue.append((nx, ny))
                    fire_time[nx][ny] = fire_time[x][y] + 1

    return fire_time


def person_bfs(person):
    person_time = [[-1] * w for _ in range(h)]
    x, y = person

    queue = deque([(x, y)])
    person_time[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y

            # base (밖으로 탈출)
            if not (0 <= nx < h and 0 <= ny < w):
                return person_time[x][y] + 1
            # 벽이거나 방문한적이 있으면 넘어감
            if graph[nx][ny] == "#" or person_time[nx][ny] != -1:
                continue
            # 불이 확산되었거나, 불 도착 시간이 이미 더 빨리 되었을 경우 사람은 못가니까 넘어감
            if fire_time[nx][ny] != -1 and fire_time[nx][ny] <= person_time[x][y] + 1:
                continue

            person_time[nx][ny] = person_time[x][y] + 1
            queue.append((nx, ny))

    return "IMPOSSIBLE"


t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    w, h = map(int, input().split())
    graph = [list(input().strip()) for _ in range(h)]
    fire = []  # 불 위치 좌표
    person = None  # 상근 좌표

    for i in range(h):
        for j in range(w):
            if graph[i][j] == "*":
                fire.append((i, j))
            elif graph[i][j] == "@":
                person = (i, j)
    fire_time = fire_bfs(fire)
    result = person_bfs(person)
    print(result)
