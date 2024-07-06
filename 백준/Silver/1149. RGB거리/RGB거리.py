n = int(input())
DP = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    DP[i][0] = min(DP[i - 1][1], DP[i - 1][2]) + DP[i][0]
    DP[i][1] = min(DP[i - 1][0], DP[i - 1][2]) + DP[i][1]
    DP[i][2] = min(DP[i - 1][0], DP[i - 1][1]) + DP[i][2]
    
print(min(DP[n - 1]))
