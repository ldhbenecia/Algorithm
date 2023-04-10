t = int(input())

for i in range(t):
  k = int(input())
  n = int(input())
  
  dp = [[0 for _ in range(n)] for _ in range(k+1)]

  for i in range(k+1):
    for j in range(n):
      if i == 0:
        dp[i][j] = j+1
      elif j == 0:
        dp[i][j] = 1
      else:
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
      
  print(dp[-1][-1])