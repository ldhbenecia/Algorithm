def dfs(v):
    stack = [v]
    visited = [False] * (n + 1)  # 1 -> 2 -> 3 -> 1 방지
    visited[v] = True
    cnt = 1

    while stack:
        x = stack.pop()
        for i in graph[x]:
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                cnt += 1

    return cnt


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

max_count = 0
result = []

for i in range(n + 1):
    cnt = dfs(i)
    if cnt > max_count: # 해킹 가능 대수 재갱신
        max_count = cnt
        result = [i]
    elif cnt == max_count:
        result.append(i)

print(*result)
