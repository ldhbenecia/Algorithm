import sys

input = sys.stdin.readline


def is_possible(row, col):
    for r in range(row):
        # 같은 열에 행이 있거나, 같은 대각선에 퀸이 있으면 False
        if graph[r] == col or abs(row - r) == abs(col - graph[r]):
            return False
    return True


def backtracking(row):
    global result

    # base
    if row == n:
        result += 1
        return

    for col in range(n):
        if is_possible(row, col):
            graph[row] = col  # 가능하면 해당 행의 열에 퀸 놓기
            backtracking(row + 1)  # 다음 행으로 이동


n = int(input())
graph = [0] * n  # 같은 행에 어차피 놓일 수 없으므로 2차원 리스트 필요 없음

result = 0
backtracking(0)
print(result)

# 퀸이 서로 공격할 수 없게 놓아야 함
# N * N 체스판에 (0, 0)부터 퀸을 놓아보고 공격이 가능할 경우 백트래킹
# 같은 행, 열, 대각에 위치하면 안됨

"""
0 0 0
0 0 0
0 0 0

(1, 1): (0, 0) - (2, 2) - (2, 0) - (0, 2)
row(행): 1
col(열): 1

(1, 1)에 퀸이 있다고 가정

0, 0: abs(1 - 0) == abs(1 - 0) -> 1
2, 2: abs(1 - 2) == abs(1 - 2) -> 1
2, 0: abs(1 - 2) == abs(1 - 0) -> 1
0, 2: abs(1 - 0) == abs(1 - 2) -> 1
"""
