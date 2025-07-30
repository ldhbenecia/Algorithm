from collections import deque


def bfs():
    queue = deque()
    visited = [
        [[False] * 61 for _ in range(61)] for _ in range(61)
    ]  # SCV는 최대 3개까지이므로 3개까지의 체력 책정

    a, b, c = 0, 0, 0
    if n == 1:
        a = hp[0]
    elif n == 2:
        a = hp[0]
        b = hp[1]
    else:
        a = hp[0]
        b = hp[1]
        c = hp[2]

    queue.append((a, b, c, 0))  # 각각 SCV의 체력과 count

    while queue:
        x, y, z, cnt = queue.popleft()

        # base
        if x == 0 and y == 0 and z == 0:
            print(cnt)
            return

        for d1, d2, d3 in patterns:
            nx = max(0, x - d1)
            ny = max(0, y - d2)
            nz = max(0, z - d3)

            if not visited[nx][ny][nz]:
                visited[nx][ny][nz] = True
                queue.append((nx, ny, nz, cnt + 1))


n = int(input())
hp = list(map(int, input().split()))
patterns = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 3, 9), (1, 9, 3)]

bfs()
