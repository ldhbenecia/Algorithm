from collections import deque


def bfs(n, m, h):
    while queue:
        z, y, x = queue.popleft()

        for d in range(6):
            nz = z + dz[d]
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= nz < h and 0 <= ny < m and 0 <= nx < n:
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append((nz, ny, nx))


n, m, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(m)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()
for i in range(h):
    for j in range(m):
        for k in range(n):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

bfs(n, m, h)

result = 0
for i in range(h):
    for j in range(m):
        for k in range(n):
            if graph[i][j][k] == 0:
                print(-1)
                exit()
            result = max(result, graph[i][j][k])

print(result - 1)
