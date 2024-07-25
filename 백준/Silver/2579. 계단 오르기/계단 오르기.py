n = int(input())
score = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(score[1])
elif n == 2:
    print(score[1] + score[2])
else:
    dp = [0] * (n + 1)
    dp[1] = score[1]
    dp[2] = score[1] + score[2]
    dp[3] = max(score[1] + score[3], score[2] + score[3])  # 한, 두 계단 중 최댓값

    for i in range(4, n + 1):
        dp[i] = max(dp[i - 3] + score[i - 1] + score[i], dp[i - 2] + score[i])

    print(dp[n])
