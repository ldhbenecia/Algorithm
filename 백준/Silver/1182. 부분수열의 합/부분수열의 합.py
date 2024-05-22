import sys
input = sys.stdin.readline

def find_subsequences(idx, current_sum):
  global count
  
  if idx == n:
    return count
  
  for i in range(idx, n):
    current_sum += nums[i]
    
    if current_sum == s:
      count += 1
    
    find_subsequences(i + 1, current_sum)
    current_sum -= nums[i]  
  

n, s = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

find_subsequences(0, 0)
print(count)