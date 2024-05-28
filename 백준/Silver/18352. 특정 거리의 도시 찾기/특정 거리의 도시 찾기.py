from collections import deque

def bfs(start):
  queue = deque([(start, 0)])
  visited[start] = True
  
  while queue:
    v, dist = queue.popleft()
    
    if dist == k:
      k_list.append(v)
    elif dist < k:
      for i in graph[v]:
        if not visited[i]:
          visited[i] = True
          queue.append((i, dist + 1))

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
k_list = [] # 최단거리가 k인 도시 저장 리스트

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

bfs(x)

if not k_list:
  print(-1)
else:
  for i in sorted(k_list):
    print(i)