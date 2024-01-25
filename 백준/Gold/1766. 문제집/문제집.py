import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)  # a가 해결해야 할 문제에 b가 선행되어야 함
  in_degree[b] += 1  # b의 진입차수 1 증가

def topology_sort():
  result = []
  heap = []

  for i in range(1, n + 1):
    if in_degree[i] == 0:  # 진입차수가 0인 노드를 큐에 추가
      heapq.heappush(heap, i)

  while heap:
    now = heapq.heappop(heap)
    result.append(now)

    for next_node in graph[now]:
      in_degree[next_node] -= 1 # 간선 제거
      if in_degree[next_node] == 0:
        heapq.heappush(heap, next_node)

  for node in result:
    print(node, end=" ")

topology_sort()