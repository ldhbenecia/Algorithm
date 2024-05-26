import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
  queue = []
  heapq.heappush(queue, (0, start))
  distance[start] = 0
  
  while queue:
    dist, now = heapq.heappop(queue)
    
    # 이미 처리된 정점일 경우 무시
    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1] # dist + 비용 w
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(queue, (cost, i[0]))

v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v + 1)]

# 최단 거리 테이블 초기화
distance = [INF] * (v + 1)

for _ in range(e):
  U, V, W = map(int, input().split())
  graph[U].append((V, W)) # # u -> v번가는 비용 = c

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리
for i in range(1, v + 1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])
    