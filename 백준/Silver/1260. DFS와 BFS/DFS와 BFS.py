from collections import deque

N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  a, b = map(int, input().split())
  
  graph[a][b] = True
  graph[b][a] = True
  
visitedDfs = [False] * (N + 1)
visitedBfs = [False] * (N + 1)

def dfs(V):
  visitedDfs[V] = True
  print(V, end=" ")
  
  for i in range(1, N + 1):
    if visitedDfs[i] == False and graph[V][i] == True:
      dfs(i)
      
def bfs(V):
  queue = deque()
  queue.append(V)
  visitedBfs[V] = True
  
  while queue:
    V = queue.popleft()
    print(V, end=" ")
    
    for i in range(1, N + 1):
      if visitedBfs[i] == False and graph[V][i] == True:
        queue.append(i)
        visitedBfs[i] = True
  
dfs(V)
print()
bfs(V)