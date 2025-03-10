from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    result[nx][ny] = result[x][y] + 1
                    queue.append((nx, ny))


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
result = [[-1] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and not visited[i][j]:
            result[i][j] = 0
            bfs(i, j)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            result[i][j] = 0

for row in result:
    print(*row)
