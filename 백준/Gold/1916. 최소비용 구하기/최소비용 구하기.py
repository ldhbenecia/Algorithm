import heapq
INF = int(1e9)

def dijkstra(start, end):
  queue = []
  heapq.heappush(queue, (0, start))
  distance[start] = 0
  
  while queue:
    dist, now = heapq.heappop(queue)
    
    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(queue, (cost, i[0]))

  return distance[end]

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

start, end = map(int, input().split())

print(dijkstra(start, end))