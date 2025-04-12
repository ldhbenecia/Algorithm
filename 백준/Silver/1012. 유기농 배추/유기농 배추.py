from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 0  # visited

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    graph[nx][ny] = 0  # visit


t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i, j)
                result += 1

    print(result)
