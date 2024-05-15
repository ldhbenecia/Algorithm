from collections import deque

def bfs(a, b):
  queue = deque([(a, 0)])
  visited[a] = 1
  
  while queue:
    position, time = queue.popleft()
    
    if position == b:
      return time
    
    # 순간이동하는 경우
    if position * 2 <= 100000 and not visited[position * 2]:
        visited[position * 2] = 1
        queue.append((position * 2, time))
        
    # 걷는 경우
    for i in [position - 1, position + 1,]:
      if 0 <= i <= 100000 and not visited[i]:
        visited[i] = 1
        queue.append((i, time + 1))

n, k = map(int, input().split())
visited = [0 for _ in range(100001)]
print(bfs(n, k))