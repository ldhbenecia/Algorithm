def backtracking(length):
  # base 조건: m만큼 수열을 생성하면 출력
  if length == m:
    print(*result)
    return
  
  for i in range(n):
    # 이전 원소와 현재 원소가 같은 경우 건너뛰기
    if i > 0 and nums[i - 1] == nums[i]: 
      continue
    result.append(nums[i])
    backtracking(length + 1)
    result.pop()
  
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = []

backtracking(0)