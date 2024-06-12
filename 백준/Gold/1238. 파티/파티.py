import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra(start):
  queue = []
  
  heapq.heappush(queue, (0, start)) # 거리, 노드
  distance = [INF] * (n + 1)
  distance[start] = 0
  
  while queue:
    dist, current = heapq.heappop(queue)
    
    if distance[current] < dist:
      continue
    
    for i in graph[current]:
      cost = dist + i[1]
      
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(queue, (cost, i[0]))
        
  return distance

answer = [0] * (n + 1) # 학생들의 소요 시간 
for i in range(1, n + 1): # 시작점 1부터 n까지
  arr = dijkstra(i) # arr에 해당 시작점의 최단경로 distance 저장
  answer[i] += arr[x] # 학생들의 소요 시간에 시작점부터 티장소까지 걸리는 시간 기록
  arr2 = dijkstra(x) # arr2에 해당 파티장소의 최단경로 distance 저장
  answer[i] += arr2[i] # 학생들의 소요 시간에 파티장소부터 시작점까지 돌아가는 시간 기록
  
  # 이 과정을 거치면 시작점에서 파티장소를 찍고 다시 돌아오는 최단 시간이 기록됨
  
# 가장 오래 걸리는 학생 소요 시간
print(max(answer))