n, m = tuple(map(int, input().split()))

# index 0을 사용하지않고 1부터 사용하기 위해
graph = [[] for _ in range(n+1)]


visited = [False for _ in range(n+1)]
vertex_cnt = 0

def dfs(vertex):
    global vertex_cnt

    for i in graph[vertex]:
        if not visited[i]:
            visited[i] = True
            vertex_cnt += 1
            dfs(i)



for i in range(m):
    v1, v2 = tuple(map(int, input().split()))

    graph[v1].append(v2)
    graph[v2].append(v1)

visited[1] = True
dfs(1)

print(vertex_cnt)