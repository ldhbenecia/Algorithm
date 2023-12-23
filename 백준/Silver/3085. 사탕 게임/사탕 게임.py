n = int(input())
board = [list(input()) for _ in range(n)]
maxCount = 0

def check():
  global maxCount
  
  for i in range(n):
    count = 1
    for j in range(n):
      if j + 1 < n and board[i][j] == board[i][j + 1]:
        count += 1
      else:
        count = 1

      if count > maxCount:
        maxCount = count
    
    count = 1
    for j in range(n):
      if j + 1 < n and board[j][i] == board[j + 1][i]:
        count += 1
      else:
        count = 1
      
      if count > maxCount:
        maxCount = count
      
  return maxCount

# 브루트포스, 완전 탐색
for i in range(n):
  for j in range(n - 1):
    # 인접한 사탕이 다를 경우 교환 (행)
    if j + 1 < n and board[i][j] != board[i][j + 1]:
      board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
      check()
      board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
    
    # 인접한 사탕이 다를 경우 교환 (열)
    if i + 1 < n and board[i][j] != board[i + 1][j]:
      board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
      check()
      board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
      
print(maxCount)
