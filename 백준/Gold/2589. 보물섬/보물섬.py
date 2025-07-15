from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    visited = [[0] * w for _ in range(h)]
    visited[x][y] = 1
    cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == 0 and graph[nx][ny] == "L":
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])

    return cnt


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

h, w = map(int, input().split())
graph = [list(input()) for _ in range(h)]


result = 0
for i in range(h):
    for j in range(w):
        if graph[i][j] == "L":
            result = max(result, bfs(i, j))

print(result - 1)


# 1. 보물을 육지에서 이동할 수 있는 곳 중에서 두 곳에 놔둬본다.
# 2. 그 중에서 가장 시간이 오래 걸린 그 위치 두 곳에 보물을 묻는다.
# 3. 거기까지 가는데 최단 거리를 구한다.
# 4. -> 이게 그냥 제일 먼거 구하면 그게 정답이다.
