from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# 꽃이 차지하는 5칸 (중심, 상, 하, 좌, 우)
dx = [0, 0, 0, 1, -1]
dy = [0, 1, -1, 0, 0]

# 가능한 중심 좌표 모으기 (가장자리 제외)
candidates = []
for i in range(1, n - 1):
    for j in range(1, n - 1):
        candidates.append((i, j))

min_cost = float(1e9)
for comb in combinations(candidates, 3):
    visited = [[False] * n for _ in range(n)]
    total = 0
    flag = True

    for x, y in comb:
        temp = 0
        for d in range(5):
            nx = x + dx[d]
            ny = y + dy[d]

            if visited[nx][ny]:
                flag = False
                break
            visited[nx][ny] = True
            temp += graph[nx][ny]
        if not flag:
            break
        total += temp
    if flag:
        min_cost = min(min_cost, total)

print(min_cost)

# 꽃을 심을 수 있는 세 위치 조합으로 탐색 (1, 1) ~ (N, N)
# 심을 수 있는 위치 값 좌푤르 통해서 꽃을 심어보고 개화될 위치에 침범하지 않는지 검사
# 검사 통과하면 값을 계산해서 min_cost를 동기화 시켜서 모두 검사
