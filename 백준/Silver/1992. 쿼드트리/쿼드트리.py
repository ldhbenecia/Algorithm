# 1 <= N <= 64
# 거의 모든 알고리즘 가능, 브루트포스, 완탐 가능

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y, n):
  is_same = True
  for i in range(x, x + n):
    for j in range(y, y + n):
      if graph[x][y] != graph[i][j]:
        is_same = False
        break
      
  if is_same:
    print(graph[x][y], end="")
  else:
    print("(", end="")
    n = n // 2
    dfs(x, y, n)
    dfs(x, y + n, n)
    dfs(x + n, y, n)
    dfs(x + n, y + n, n)
    print(")", end="")

dfs(0, 0, n)