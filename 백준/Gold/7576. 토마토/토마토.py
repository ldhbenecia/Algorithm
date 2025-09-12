from collections import deque


def bfs():
    queue = deque()

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                    graph[nx][ny] = graph[x][y] + 1


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * n for _ in range(m)]


# 저장될 때부터 다 익어있는지 확인
flag = True  # 다 익음이 디폴트
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            flag = False  # 다 익어있지않음

if flag:
    print(0)
    exit()

# 시작 좌표를 주지 않는 이유
# 주면 그 좌포에서 상하좌우로 퍼지기 시작하는데
# 다른 익은 토마토가 있는 지점에서도 동시에 퍼지기 시작해야됨
bfs()

result = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            print(-1)
            exit()
        result = max(result, graph[i][j])

print(result - 1)
