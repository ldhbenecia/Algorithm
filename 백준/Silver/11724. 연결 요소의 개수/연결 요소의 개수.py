from collections import deque


def bfs(x):
    queue = deque([x])
    visited[x] = True

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

count = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i)
        count += 1


print(count)
