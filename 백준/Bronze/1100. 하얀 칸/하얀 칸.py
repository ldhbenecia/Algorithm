board = [input() for _ in range(8)]
count = 0

for i in range(len(board)):
  for j in range(len(board)):
    if i % 2 == 0 and j % 2 == 0:
      if board[i][j] == 'F':
        count += 1
    elif i % 2 != 0 and j % 2 != 0:
      if board[i][j] == 'F':
        count += 1
      
print(count)