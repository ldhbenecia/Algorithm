from collections import deque


# 녹일 치즈 선발
def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    cnt = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    queue.append((nx, ny))
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    cnt += 1
                visited[nx][ny] = True

    melt_history.append(cnt)
    return cnt


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

melt_history = []
time = 0

# 녹일 치즈가 없을 때까지 반복
while True:
    visited = [[False] * m for _ in range(n)]  # 반복 때마다 초기화 해주어야 함

    remain = bfs(0, 0)  # 남은 치즈 칸의 개수
    if not remain:
        print(time)
        print(melt_history[-2])  # 모두 녹기 전 칸의 개수
        break

    time += 1
