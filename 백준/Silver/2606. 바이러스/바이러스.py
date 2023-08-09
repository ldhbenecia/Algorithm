n = int(input())
m = int(input())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  
  # 인접 노드 연결
  graph[a][b] = True
  graph[b][a] = True
  
visited = [False] * (n + 1)

v = 1 # 1번 컴퓨터가 바이러스 걸림

def dfs(v):
  visited[v] = True
  
  for i in range(1, n + 1):
    if visited[i] == False and graph[v][i] == True:
      dfs(i)
      
dfs(v)
print(sum(visited) - 1)