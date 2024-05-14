from collections import deque

def bfs(a, b):
  queue = deque([a])
  visited = [0 for _ in range(n + 1)]
  
  visited[a] = 1
  
  while queue:
    people = queue.popleft()
    
    if people == b:
      return visited[b] - 1
    
    for i in graph[people]:
      if visited[i] == 0:
        queue.append(i)
        visited[i] = visited[people] + 1
        
  return -1

n = int(input())
a, b = map(int, input().split()) # 촌수를 구해야 하는 사람의 번호
m = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(m):
  x, y = map(int, input().split()) # 부모, 자식
  graph[x].append(y)
  graph[y].append(x)
  
print(bfs(a, b))
  
# 노드를 서로 이어준다.
# BFS 탐색을 해서 간선의 개수만큼이 촌수이다.
# 탐색을 했는데 간선의 개수가 0인 경우 이어져있지않다는 뜻으로 -1