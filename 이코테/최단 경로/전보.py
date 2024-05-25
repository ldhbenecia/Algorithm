import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
  X, Y, Z = map(int, input().split()) # X -> Y로 Z시간만큼  
  
  # X에서 Y로 가는 비용 = Z
  graph[X].append((Y, Z))
  
def dijkstra(start):
  queue = []
  heapq.heappush(queue, (0, start))
  distance[start] = 0
  
  while queue:
    dist, current = heapq.heappop(queue)
    if distance[current] < dist:
      continue
    
    for i in graph[current]:
      cost = dist + i[1] # dist는 이전 노드의 비용, i[1]은 현재 노드의 비용
      # 현재 노드를 거치면 이동거리가 더 짧은 경우
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(queue, (cost, i[0]))
        
dijkstra(C)      

count = 0
max_distance = 0
for i in distance:
  if i != INF:
    count += 1
    max_distance = max(max_distance, i)
    
print(count - 1, max_distance)

"""
입력 예시
3 2 1
1 2 4
1 3 2

출력 예시
2 4
"""
