from itertools import combinations


def to_distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

home = []
store = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i, j))
        if graph[i][j] == 2:
            store.append((i, j))

min_total = float("inf")
for store_position in combinations(store, m):  # m개 치킨집 선택
    total = 0
    for h in home:
        min_distance = 1e9
        for sp in store_position:
            distance = to_distance(h[0], h[1], sp[0], sp[1])
            min_distance = min(min_distance, distance)
        total += min_distance

    if total < min_total:
        min_total = total

print(min_total)
