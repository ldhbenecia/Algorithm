from collections import deque

n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  
  # 인접한 연결 노드 True 처리
  graph[a][b] = True
  graph[b][a] = True
  
visitedDfs = [False] * (n + 1) # DFS 방문기록
visitedBfs = [False] * (n + 1) # BFS 방문기록

def dfs(v):
  visitedDfs[v] = True
  print(v, end=' ')
  
  for i in range(1, n + 1):
    if visitedDfs[i] == False and graph[v][i] == True:
      dfs(i)
      
def bfs(v):
  queue = deque([v])
  visitedBfs[v] = True
  
  while queue:
    v = queue.popleft()
    print(v, end=' ')
    
    for i in range(1, n + 1):
      if visitedBfs[i] == False and graph[v][i] == True:
        queue.append(i)
        visitedBfs[i] = True
      
dfs(v)
print()
bfs(v)