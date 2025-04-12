from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    graph[x][y] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < m and 0 <= ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1

    return cnt


m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):  # y가 행 (row)
        for x in range(x1, x2):  # x가 열 (col)
            graph[y][x] = 1

result = []
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result.append(bfs(i, j))

result.sort()
print(len(result))
print(*result)
