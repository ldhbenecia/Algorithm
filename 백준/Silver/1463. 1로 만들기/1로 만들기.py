import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * (n + 1)

# dp[1] = 0, 처음부터 1이니까 연산 안하니까 0으로 초기화
# for문은 2부터 실행

# 10 -> 9 -> 3 -> 1
# 9 -> 3 -> 1
# 10을 구할 때 9의 결과를, 9를 구할 때 3의 결과를 재사용
# 이를 DP 테이블에 기록해두고 재활용
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # 1을 빼는 경우와 나누었을 때 중 최솟값

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])
