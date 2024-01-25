import sys
sys.setrecursionlimit(100000)

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
  a, b = map(int, input().split())
  
  graph[a].append(b)
  graph[b].append(a)
  
def dfs(start):
  for i in graph[start]:
    if visited[i] == False:
      visited[i] = start
      dfs(i)
      
dfs(1)

for i in range(2, n + 1):
  print(visited[i])
