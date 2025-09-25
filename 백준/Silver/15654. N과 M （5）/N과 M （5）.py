def backtracking(depth):
    # base
    if depth == m:
        print(*temp)
        return

    for i in range(len(nums)):
        if nums[i] in temp:
            continue
        temp.append(nums[i])
        backtracking(depth + 1)
        temp.pop()


n, m = map(int, input().split())
nums = list(map(int, input().split()))

temp = []
nums.sort()
backtracking(0)
