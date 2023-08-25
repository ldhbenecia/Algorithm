n, m = map(int, input().split())
graph = [[False] for _ in range(n + 1)] # 1부터 시작하므로 (0 거르기)

visited = [False] * (n + 1)

for _ in range(m):
  u, v = map(int, input().split())
  
  graph[u].append(v)
  graph[v].append(u)
  

def dfs(start):
  visited[start] = True
  
  for i in graph[start]:
    if visited[i] is False:
      visited[i] = True
      dfs(i)
  
cnt = 0
for i in range(1, n + 1):
  if visited[i] is False:
    cnt += 1
    dfs(i)
  
print(cnt)