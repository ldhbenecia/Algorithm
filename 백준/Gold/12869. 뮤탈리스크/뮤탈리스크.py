from collections import deque


def bfs():
    queue = deque()
    visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]

    # 체력 초기값 세팅 (없으면 0)
    a, b, c = 0, 0, 0
    if len(hp) >= 1:
        a = hp[0]
    if len(hp) >= 2:
        b = hp[1]
    if len(hp) == 3:
        c = hp[2]

    queue.append((a, b, c, 0))
    visited[a][b][c] = True

    while queue:
        x, y, z, cnt = queue.popleft()

        if x == 0 and y == 0 and z == 0:
            print(cnt)
            return

        # 공격 받은 후 SCV 체력 측정 - 0 이하는 파괴이므로 0으로 지정
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
