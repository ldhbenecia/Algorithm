from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True

    weight = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if (
                0 <= nx < n
                and 0 <= ny < m
                and not visited[nx][ny]
                and graph[nx][ny] == 1
            ):
                visited[nx][ny] = True
                queue.append((nx, ny))
                weight += 1

    return weight


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

pic = 0  # 그림 개수
result = 0  # 넓이
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            result = max(result, bfs(i, j))
            pic += 1

print(pic)
print(result)
