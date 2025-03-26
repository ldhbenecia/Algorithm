from collections import deque


def dfs(x):
    stack = [x]
    visited[x] = True
    count = 0

    while stack:
        v = stack.pop()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                count += 1
    return count


def bfs(x):
    queue = deque([x])
    visited[x] = True
    count = 0

    while queue:
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                count += 1

    return count


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)

# print(bfs(1))
print(dfs(1))
