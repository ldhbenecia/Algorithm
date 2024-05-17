from collections import deque

def bfs(a, b):
  queue = deque([(a, 0)])
  
  while queue:
    position, time = queue.popleft()
    
    if position == b:
      idx = position
      while idx != a:
        path.append(idx)
        idx = visited[idx]
      path.append(a)
      path.reverse()
      return time, path
    
    for i in [2 * position, position - 1, position + 1]:
      if 0 <= i < 100001 and visited[i] == -1:
        visited[i] = position
        queue.append((i, time + 1))
      
n, k = map(int, input().split())
visited = [-1 for _ in range(100001)]
path = []

time, route = bfs(n, k)
print(time)
print(" ".join(map(str, route)))