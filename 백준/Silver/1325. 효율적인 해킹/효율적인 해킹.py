from collections import deque

def bfs(start):
  queue = deque([start])
  visited[start] = True
  count = 1
  
  while queue:
    v = queue.popleft()
    
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True
        count += 1
  return count

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[b].append(a)

result = []
max_count = -1e9
for i in range(1, n + 1):
  visited = [False] * (n + 1)
  count = bfs(i)
  if max_count < count:
    max_count = count
    # append로 처리 시 이후 최댓값이 바뀔 수도 있으니 최댓 값이 나오면 그 값으로 초기화
    result = [i]
  elif max_count == count:
    result.append(i)
  
print(*sorted(result))
  