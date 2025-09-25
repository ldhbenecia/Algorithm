import sys

input = sys.stdin.readline


def backtracking(depth, start):
    # base
    if depth == m:
        print(*temp)
        return

    for i in range(start, n):
        temp.append(nums[i])
        backtracking(depth + 1, i)
        temp.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

temp = []

backtracking(0, 0)
