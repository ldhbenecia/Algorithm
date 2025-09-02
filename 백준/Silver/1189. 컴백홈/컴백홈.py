def dfs(x, y, dist):
    global result

    # base
    if (x, y) == (end_x, end_y):
        if dist == k:
            result += 1
        return

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < r and 0 <= ny < c:
            if not visited[nx][ny] and graph[nx][ny] != "T":
                visited[nx][ny] = True
                dfs(nx, ny, dist + 1)
                visited[nx][ny] = False


r, c, k = map(int, input().split())
graph = [list(input()) for _ in range(r)]

start_x, start_y = r - 1, 0
end_x, end_y = 0, c - 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * c for _ in range(r)]
visited[start_x][start_y] = True

result = 0
dfs(start_x, start_y, 1)

print(result)
