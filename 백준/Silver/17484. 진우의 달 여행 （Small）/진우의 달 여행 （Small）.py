n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[[1e9] * 3 for _ in range(m)] for _ in range(n)]

# dp 첫 행 초기화
for j in range(m):
    for d in range(3):
        dp[0][j][d] = board[0][j]

dy = [-1, 0, 1]

# 아래로 이동하면서 최소 합을 가지는 경로 찾기
for i in range(1, len(board)):
    for j in range(len(board[i])):
        # 이전 행에서 온 방향으로 이동 x
        for d in range(3):  # 현재 향하는 방향
            prev_x = i - 1  # 이전 행 좌표
            prev_j = j + dy[d]  # 이전 열 계산 (현재 이동 방향 기준)

            if 0 <= prev_j < m:
                for prev_d in range(3):
                    if prev_d != d:  # 같은 방향 x
                        dp[i][j][d] = min(
                            dp[i][j][d], board[i][j] + dp[prev_x][prev_j][prev_d]
                        )

result = 1e9
# 결과 값 중 최솟값 찾기
for j in range(m):  # 마지막 행의 모든 열 j 반복
    for d in range(3):  # 3가지 방향에 대해 반복
        result = min(result, dp[n - 1][j][d])

print(result)
