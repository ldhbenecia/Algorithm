n = int(input())
row = [0] * n
count = 0

def check(x):
  for i in range(x):
    # 같은 행 대각인지 (행차이 == 열차이)
    if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
      return False
  return True
    
def backtracking(x):
  global count

  if x == n:
    count += 1
    return
  else:
    for i in range(n):
      row[x] = i
      if check(x):
        backtracking(x + 1)
      
      
backtracking(0)
print(count)