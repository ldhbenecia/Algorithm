from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  in_degree[b] += 1

def topology_sort():
  queue = deque()
  result = []
  
  for i in range(1, n + 1):
    if in_degree[i] == 0:
      queue.append(i)
  
  while queue:
    now = queue.popleft()
    result.append(now)
    
    for i in graph[now]:
      in_degree[i] -= 1 # 해당 정점과 연결되어있는 간선 제거
      if in_degree[i] == 0: # 진입 차수가 0인 정점을 큐에 삽입
        queue.append(i)
        
  for i in result:
    print(i, end =" ")
  
topology_sort()