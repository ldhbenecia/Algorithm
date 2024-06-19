def solution(land):
    dp = land
    
    for i in range(1, len(land)):
        for j in range(4):
            dp[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(dp[-1])