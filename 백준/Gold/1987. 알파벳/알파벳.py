def dfs(x, y):
  stack = [(x, y, graph[x][y], 1)]
  max_dist = 0
  
  while stack:
    x, y, alphabet, dist = stack.pop()
    max_dist = max(max_dist, dist)
    
    for i in range(4):
      nx = dx[i] + x
      ny = dy[i] + y
      
      if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] not in alphabet:
        stack.append((nx, ny, alphabet + graph[nx][ny], dist + 1))
  
  return max_dist
      
r, c = map(int, input().split())
graph = [input() for _ in range(r)]

visited = [False for _ in range(26)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(dfs(0, 0))