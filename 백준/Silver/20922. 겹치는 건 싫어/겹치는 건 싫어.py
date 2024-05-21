import sys
input = sys.stdin.readline

n, k = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 0
answer = 0
counter = [0] * (max(nums) + 1)

while end < n:
  if counter[nums[end]] < k:
    counter[nums[end]] += 1
    end += 1
  else:
    counter[nums[start]] -= 1
    start += 1
  
  answer = max(end - start, answer)
  
print(answer)