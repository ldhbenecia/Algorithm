def backtracking(length, start):
  if length == m:
    print(*result)
    return
  
  for i in range(start, n):
    if i > 0 and nums[i - 1] == nums[i]:
      continue
    result.append(nums[i])
    backtracking(length + 1, i)
    result.pop()
    

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = []

backtracking(0, 0)