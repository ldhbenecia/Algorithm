import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs(start, end):
    queue = deque()
    visited = [[[False] * c for _ in range(r)] for _ in range(l)]
    sz, sy, sx = start
    queue.append((sz, sy, sx, 0))
    visited[sz][sy][sx] = True

    while queue:
        z, y, x, dist = queue.popleft()
        if (z, y, x) == end:
            return dist

        for d in range(6):
            nz = dz[d] + z
            ny = dy[d] + y
            nx = dx[d] + x

            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c:
                if not visited[nz][ny][nx] and graph[nz][ny][nx] != "#":
                    queue.append((nz, ny, nx, dist + 1))
                    visited[nz][ny][nx] = True

    return -1


while True:
    l, r, c = map(int, input().split())

    # base
    if l == 0 and r == 0 and c == 0:
        break

    start = end = None
    graph = []

    for z in range(l):
        floor = []
        for y in range(r):
            row = list(input().strip())
            for x in range(c):
                if row[x] == "S":
                    start = (z, y, x)
                elif row[x] == "E":
                    end = (z, y, x)
            floor.append(row)
        graph.append(floor)
        input()

    result = bfs(start, end)
    if result == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {result} minute(s).")
