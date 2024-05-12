from collections import deque

def bfs(start):
  queue = deque([start])
  visited = [0] * n
  
  while queue:
    v = queue.popleft()
    
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = 1

  return visited
  
n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
  row = list(map(int, input().split()))
  for j in range(n):
    if row[j] == 1:
      graph[i].append(j)
      
for i in range(n):
  print(*bfs(i))

'''
0 1 0
0 0 1
1 0 0

[1]
[2]
[0]

0번째 노드가 갈 수 있는 노드는 1번
1번째 노드가 갈 수 있는 노드는 2번
2번째 노드가 갈 수 있는 노드는 0번

0 -> 1 -> 2 -> 0
'''
