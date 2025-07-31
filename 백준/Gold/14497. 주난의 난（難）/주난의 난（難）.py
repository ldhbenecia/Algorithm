from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                # 점프할 수 있는 위치: '1' 혹은 '#'
                if graph[nx][ny] == "1" or graph[nx][ny] == "#":
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                # 점프할 수 없는 위치(이동만 가능한 곳): '0'
                elif graph[nx][ny] == "0":
                    visited[nx][ny] = visited[x][y]
                    queue.appendleft((nx, ny))


n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[-1] * m for _ in range(n)]

bfs(x1 - 1, y1 - 1)
print(visited[x2 - 1][y2 - 1])
