from collections import deque


def bfs(start):
    dist = [-1] * (N + 1)
    queue = deque([start])
    dist[start] = 0

    while queue:
        v = queue.popleft()

        for nx in graph[v]:
            if dist[nx] == -1:
                dist[nx] = dist[v] + 1
                queue.append(nx)

    return dist


N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

best_sum = float("inf")
best_node = 1

for i in range(1, N + 1):
    dist = bfs(i)
    total = sum(dist[1:])  # 연결 그래프라면 -1 없음
    if total < best_sum:
        best_sum = total
        best_node = i

print(best_node)
