import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split()) # a: 출발 노드, b: 도착 노드, c: 간선 가중치
  
  # a번 노드에서 b번 노드로 가는 비용 = c
  graph[a].append((b, c))

def dijkstra(start):
  queue = []
  
  # 시작 노드로 가기 위한 최단 경로 0으로 설정 (거리, 노드)
  heapq.heappush(queue, (0, start))
  distance[start] = 0
  while queue:
    # 거리, 현재 노드 pop
    dist, current = heapq.heappop(queue)
    
    # 이미 처리된 노드일 경우 무시
    if distance[current] < dist:
      continue
    
    # 현재 노드와 인접 노드 확인
    for i in graph[current]:
      cost = dist + i[1] # 0은 거리, 1은 노드
      # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
      if cost < distance[i[0]]: # 기존에 입력되어있는 값보다 크다면
        distance[i[0]] = cost
        heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리
for i in range(1, n + 1):
  # 도달할 수 없는 경우 INFINITY 출력
  if distance[i] == INF:
    print("INFINITY")
  else:
    print(distance[i])

"""
입력 예시
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2

출력 예시
0
2
3
1
2
4
"""
