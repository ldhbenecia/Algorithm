from collections import deque

def bfs(start):
  queue = deque([(start)])
  visited[start] = 0 # 시작 층은 횟수 0으로
  
  while queue:
    v = queue.popleft()
    
    if v == G:
      return visited[v]
    
    for i in (v + U, v - D):
      if 0 < i <= F and visited[i] == -1:
        visited[i] = visited[v] + 1
        queue.append(i)
        
  return 'use the stairs'

F, S, G, U, D = map(int, input().split())
visited = [-1 for _ in range(F + 1)]
print(bfs(S))
