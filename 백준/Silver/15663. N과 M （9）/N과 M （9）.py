import sys

input = sys.stdin.readline


def backtracking(depth):
    # base
    if depth == m:
        print(*temp)
        return

    last = 0
    for i in range(n):
        if visited[i]:
            continue
        if last == nums[i]:
            continue

        visited[i] = True
        temp.append(nums[i])
        last = nums[i]
        backtracking(depth + 1)
        temp.pop()
        visited[i] = False


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n

temp = []
backtracking(0)
