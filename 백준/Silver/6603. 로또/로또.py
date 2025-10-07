import sys

input = sys.stdin.readline


def backtracking(depth, idx):
    # base
    if depth == 6:
        print(*temp)
        return

    for i in range(idx, len(case)):
        temp.append(case[i])
        backtracking(depth + 1, i + 1)
        temp.pop()


# 입력은 여러 테스트케이스, 0이 종료 조건
first_case = True
while True:
    cmd = list(map(int, input().split()))

    # base
    if not cmd:
        break

    if cmd[0] == 0:
        break

    case = cmd[1:]
    case.sort()

    temp = []

    if not first_case:
        print()
    first_case = False

    backtracking(0, 0)
