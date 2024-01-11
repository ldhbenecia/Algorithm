import heapq
INF = int(1e9)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dijkstra():
  q = []
  heapq.heappush(q, (graph[0][0], 0, 0))
  distance[0][0] = graph[0][0]
  
  while q:
    dis, x, y = heapq.heappop(q)
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if (0 <= nx < n) and (0 <= ny < n):
        cost = dis + graph[nx][ny]
      
        if distance[nx][ny] > cost:
          distance[nx][ny] = cost
          heapq.heappush(q, (cost, nx, ny))

turn = 0
while True:
  turn += 1
  n = int(input())
  graph = [list(map(int, input().split())) for _ in range(n)]
  distance = [[INF] * n for _ in range(n)]

  if n == 0:
    break
  
  dijkstra()
  print(f'Problem {turn}: {distance[n-1][n-1]}')
  