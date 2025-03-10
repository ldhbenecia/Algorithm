from collections import deque


def dfs(v):
    visited_dfs[v] = True
    print(v, end=" ")
    for i in range(n + 1):
        if not visited_dfs[i] and graph[v][i]:
            dfs(i)


def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in range(n + 1):
            if not visited_bfs[i] and graph[v][i]:
                visited_bfs[i] = True
                queue.append(i)


n, m, v = map(int, input().split())

# 간선이 연결되어있다.
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 각 경로 방문 기록 저장 리스트
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

dfs(v)
print()
bfs(v)
