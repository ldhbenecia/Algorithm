def dfs(x):
    stack = [x]
    visited[x] = True

    while stack:
        v = stack.pop()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)


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
        dfs(i)
        count += 1


print(count)
