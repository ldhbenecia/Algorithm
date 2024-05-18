from collections import deque

def bfs(start):
  queue = deque([(start)])
  visitedBfs[start] = True
  
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    
    for i in sorted(graph[v]):
      if not visitedBfs[i]:
        visitedBfs[i] = True
        queue.append(i)
        
def dfs(start):
  visitedDfs[start] = True
  print(start, end = ' ')
  
  for i in sorted(graph[start]):
    if not visitedDfs[i]:
      dfs(i)
  
n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
  
visitedBfs = [False] * (n + 1)
visitedDfs = [False] * (n + 1)
dfs(v)
print()
bfs(v)