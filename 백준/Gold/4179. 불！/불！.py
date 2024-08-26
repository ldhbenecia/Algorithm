from collections import deque

def bfs():
    queue_j = deque()
    queue_f = deque()

    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'J':
                queue_j.append((i, j))
                visited_j[i][j] = 0
            elif graph[i][j] == "F":
                queue_f.append((i, j))
                visited_f[i][j] = 0

    while queue_f:
        x, y = queue_f.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != "#" and visited_f[nx][ny] == -1:
                    visited_f[nx][ny] = visited_f[x][y] + 1
                    queue_f.append((nx, ny))

    # 사람의 BFS
    while queue_j:
        x, y = queue_j.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if graph[nx][ny] != "#" and visited_j[nx][ny] == -1:
                    # 불이 아직 도달하지 않았거나 불이 도달한 시간보다 더 늦게 도달할 수 있는 경우
                    if visited_f[nx][ny] == -1 or visited_f[nx][ny] > visited_j[x][y] + 1:
                        visited_j[nx][ny] = visited_j[x][y] + 1
                        queue_j.append((nx, ny))
            else:
                return visited_j[x][y] + 1

    return "IMPOSSIBLE"


r, c = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited_j = [[-1] * c for _ in range(r)]
visited_f = [[-1] * c for _ in range(r)]

print(bfs())
