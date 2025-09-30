import sys

input = sys.stdin.readline


def backtracking(depth, start):
    # base
    if depth == m:
        print(*temp)
        return

    prev = None
    for i in range(start, n):
        if prev == nums[i]:
            continue

        if temp and nums[i] < temp[-1]:
            continue

        prev = nums[i]  # 동기화
        temp.append(nums[i])
        backtracking(depth + 1, i + 1)
        temp.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

temp = []
backtracking(0, 0)
