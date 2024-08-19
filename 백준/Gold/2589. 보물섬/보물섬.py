from collections import deque

def bfs(x, y):
    queue = deque([(x, y, 0)])
    visited = [[False] * w for _ in range(l)]
    visited[x][y] = True
    max_dist = 0

    while queue:
        x, y, cnt = queue.popleft()
        max_dist = max(max_dist, cnt)

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < l and 0 <= ny < w:
                if graph[nx][ny] == 'L' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt + 1))

    return max_dist

l, w = map(int, input().split())
graph = [list(input()) for _ in range(l)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = []
for i in range(l):
    for j in range(w):
        if graph[i][j] == 'L':
            result.append(bfs(i, j))

print(max(result))
