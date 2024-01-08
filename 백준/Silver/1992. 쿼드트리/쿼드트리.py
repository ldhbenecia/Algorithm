n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def backtracking(r, c, n):
  is_same = True

  for i in range(r, r + n):
    for j in range(c, c + n):
      if graph[r][c] != graph[i][j]:
        is_same = False
        break

  if is_same:
    print(graph[r][c], end="")
  else:
    half_size = n // 2
    print("(", end="")
    backtracking(r, c, half_size)
    backtracking(r, c + half_size, half_size)
    backtracking(r + half_size, c, half_size)
    backtracking(r + half_size, c + half_size, half_size)
    print(")", end="")
  
backtracking(0, 0, n)