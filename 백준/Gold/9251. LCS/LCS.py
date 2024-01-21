a = input()
b = input()

col, row = len(a), len(b)
dp = [[0] * (row + 1) for _ in range(col + 1)]

for i in range(1, col + 1):
  for j in range(1, row + 1):
    if a[i - 1] == b[j - 1]:
      dp[i][j] = dp[i - 1][j - 1] + 1
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
      
print(dp[-1][-1])