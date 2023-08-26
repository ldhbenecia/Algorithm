from collections import deque

def bfs(v):
  queue = deque([v])
  
  while queue:
    v = queue.popleft()
    
    if v == k:
      return graph[v]
    else:
      for i in (v - 1, v + 1, 2 * v):
        if 0 <= i <= 100000 and not graph[i]:
          graph[i] = graph[v] + 1
          queue.append(i)
  
n, k = map(int, input().split())
graph = [0] * 100001


print(bfs(n)) # n(5)가 시작점이므로 알규먼트에 5 삽입
