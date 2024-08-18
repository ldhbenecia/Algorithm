from itertools import combinations

def calculator(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            home.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

result = float("inf")
for i in combinations(chicken, m):
    total_distance = 0
    for j in home:
        distance = float('inf')
        for k in i:
            distance = min(distance, calculator(j, k))
        total_distance += distance
    result = min(result, total_distance)
print(result)
