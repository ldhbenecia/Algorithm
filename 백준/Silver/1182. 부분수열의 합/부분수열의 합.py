import sys

input = sys.stdin.readline


def backtracking(idx, sum):
    global result

    # base
    if idx == n:
        if sum == s:
            result += 1
        return

    # 현재 원소 포함
    backtracking(idx + 1, sum + nums[idx])
    # 현재 원소 미포함
    backtracking(idx + 1, sum)


n, s = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
backtracking(0, 0)

# 공집합(아무것도 선택하지 않은 경우)은 제외해야 함
if s == 0:
    result -= 1

print(result)
