def dfs(x, y, color):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] == color:
                    stack.append((nx, ny))
                    visited[nx][ny] = True


def dfs_rg(x, y, color):
    stack = [(x, y)]
    visited[x][y] = True

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if color in "RG" and graph[nx][ny] in "RG":  # R, G 묶음
                    stack.append((nx, ny))
                    visited[nx][ny] = True
                elif color == "B" and graph[nx][ny] == "B":
                    stack.append((nx, ny))
                    visited[nx][ny] = True


n = int(input())
graph = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 일반인
visited = [[False] * n for _ in range(n)]
normal = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, graph[i][j])
            normal += 1

# 적록색약
visited = [[False] * n for _ in range(n)]
unnormal = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs_rg(i, j, graph[i][j])
            unnormal += 1


print(normal, unnormal)
