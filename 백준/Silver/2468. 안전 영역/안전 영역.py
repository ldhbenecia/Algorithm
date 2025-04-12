from collections import deque


def bfs(x, y, h, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] > h:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_height = max(map(max, graph))
result = 0

for h in range(max_height + 1):  # 안오는 경우를 위해 0부터 시작함
    visited = [[False] * n for _ in range(n)]
    safe_zone = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and graph[i][j] > h:
                bfs(i, j, h, visited)
                safe_zone += 1

    result = max(result, safe_zone)

print(result)
