n, s = map(int, input().split())
nums = list(map(int, input().split()))
left, right = 0, 0
part_sum = 0
min_length = 1e9

while True:
  if part_sum >= s:
    min_length = min(min_length, right - left)
    part_sum -= nums[left]
    left += 1
  elif right == n:
    break
  else:
    part_sum += nums[right]
    right += 1
    
if min_length == 1e9:
  print(0)
else:
  print(min_length)