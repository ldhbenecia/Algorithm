import sys
sys.setrecursionlimit(100000)

def dfs(start):
  for i in graph[start]:
    if parent[i] == 0:
      parent[i] = start
      dfs(i)

n = int(input())

graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for _ in range(1, n):
  n1, n2 = map(int, input().split())
  graph[n1].append(n2)
  graph[n2].append(n1)
  
dfs(1)
  
for i in range(2, n + 1):
  print(parent[i])