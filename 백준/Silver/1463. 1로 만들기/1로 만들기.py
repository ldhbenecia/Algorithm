n = int(input())
dp = [0] * (n + 1)

# DP 테이블 생성 시 n+1 사이즈로 생성하였으므로 첫 배열 버림
# 1의 경우 무조건 0이기 때문에 for문 범위를 2부터 n+1까지 설정
for i in range(2, n + 1):
  dp[i] = dp[i - 1] + 1
  
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i//3] + 1)
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i//2] + 1)
  
print(dp[n])