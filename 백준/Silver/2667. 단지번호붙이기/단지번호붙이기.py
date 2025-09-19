from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    home = 1

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y

            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    home += 1

    return home


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = 0
group = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and not visited[i][j]:
            home_cnt = bfs(i, j)
            group.append(home_cnt)
            total += 1

print(total)
for i in sorted(group):
    print(i)
