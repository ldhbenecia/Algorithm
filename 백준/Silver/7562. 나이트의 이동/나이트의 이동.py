from collections import deque

t = int(input())

# 나이트 이동 가능 방향
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(t):
    l = int(input())
    graph = [[0] * l for _ in range(l)]
    visited = [[False] * l for _ in range(l)]

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    queue = deque([(x1, y1)])
    visited[x1][y1] = True

    while queue:
        x, y = queue.popleft()

        # base
        if x == x2 and y == y2:
            print(graph[x][y])
            break

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
