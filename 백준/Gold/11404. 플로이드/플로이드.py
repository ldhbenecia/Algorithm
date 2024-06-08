import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

for _ in range(m):
  a, b, c = map(int, input().split())
  
  # 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.
  graph[a][b] = min(c, graph[a][b])
  
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
      
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print(0, end = ' ')
    else:
      print(graph[a][b], end = ' ')
  print()