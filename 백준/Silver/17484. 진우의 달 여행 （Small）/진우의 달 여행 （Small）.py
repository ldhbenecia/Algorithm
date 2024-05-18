def dfs(col, row, last_move):
  
  # 종료 조건
  if col == n - 1:
    return graph[col][row]
  
  min_cost = 1e9
  
  for i in range(3):
    nc = col + 1
    nr = row + dy[i]
    
    if 0 <= nr < m and i != last_move:
      cost = graph[col][row] + dfs(nc, nr, i)
      min_cost = min(min_cost, cost)
  
  return min_cost

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 왼쪽 아래, 아래, 오른쪽 아래
dy = [-1, 0, 1]
cost = 1e9

for i in range(m):
  cost = min(dfs(0, i, -1), cost) # 시작 행 0, 시작 열 i, 이전 움직임 -1
  
print(cost)