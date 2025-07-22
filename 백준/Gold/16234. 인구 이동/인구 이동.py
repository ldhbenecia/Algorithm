def dfs(x, y):
    stack = [(x, y)]
    union = [(x, y)]
    total = peoples[x][y]
    visited[x][y] = True

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(peoples[x][y] - peoples[nx][ny]) <= r:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
                    union.append((nx, ny))
                    total += peoples[nx][ny]

    return total, union


n, l, r = map(int, input().split())
peoples = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

while True:
    visited = [[False] * n for _ in range(n)]
    is_moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                total, union = dfs(i, j)
                # 인구 이동이 일어났으면 해당 평균 인구수로 채워주기
                if len(union) > 1:
                    is_moved = True
                    new_pop = total // len(union)
                    for x, y in union:
                        peoples[x][y] = new_pop

    if not is_moved:
        break
    result += 1

print(result)
