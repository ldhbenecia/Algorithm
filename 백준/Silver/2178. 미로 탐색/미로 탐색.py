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
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1  # 이전에 건너오기 전 값 +1

    return graph[n - 1][m - 1]


n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
