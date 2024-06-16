import sys
input = sys.stdin.readline

def dfs(start, cnt):
  visited[start] = True
  
  for i in graph[start]:
    if not visited[i]:
      cnt = dfs(i, cnt + 1)
      
  return cnt

t = int(input())

for _ in range(t):
  n, m = map(int, input().split())
  graph = [[] for _ in range(n + 1)]
  for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
  
  visited = [False] * (n + 1)
  count = dfs(1, 0)
  print(count)