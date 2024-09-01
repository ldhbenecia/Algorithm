from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if graph[nx][ny] == "1" or graph[nx][ny] == "#":
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

                elif graph[nx][ny] == "0":
                    queue.appendleft((nx, ny))
                    visited[nx][ny] = visited[x][y]


n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs(x1 - 1, y1 - 1)
print(visited[x2 - 1][y2 - 1])
