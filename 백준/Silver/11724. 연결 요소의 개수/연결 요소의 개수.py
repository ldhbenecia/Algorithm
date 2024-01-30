from collections import deque

def bfs(start):
  queue = deque([start])
  visited[start] = True
  
  while queue:
    v = queue.popleft()
    
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

for i in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)
  
for i in range(1, n + 1):
  if not visited[i]:
    bfs(i)
    count += 1
    
print(count)