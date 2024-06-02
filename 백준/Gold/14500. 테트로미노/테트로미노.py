def dfs(x, y, turn, total):
  global max_sum
    
  if turn == 4:
    max_sum = max(max_sum, total)
    return
  
  for i in range(4):
    nx = dx[i] + x
    ny = dy[i] + y
    
    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
      visited[nx][ny] = True
      dfs(nx, ny, turn + 1, total + board[nx][ny])
      visited[nx][ny] = False
    
def check_special(x, y):
  global max_sum
  
  # ㅗ, ㅜ, ㅓ, ㅏ 모양 (상하좌우 네 칸 중 세 칸을 더하는 방법)
  for i in range(4):
    total = board[x][y] # 초기값 (시작지점)
    for j in range(3):
      t = (i + j) % 4
      nx = dx[t] + x
      ny = dy[t] + y
      
      if not (0 <= nx < n and 0 <= ny < m):
        total = 0
        break
      total += board[nx][ny]
    
    max_sum = max(max_sum, total)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

max_sum = 0
for i in range(n):
  for j in range(m):
    visited[i][j] = True
    dfs(i, j, 1, board[i][j])
    visited[i][j] = False
    check_special(i, j)

print(max_sum)