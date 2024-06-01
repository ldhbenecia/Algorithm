def binary_search(start, end):
  while start <= end:
    mid = (start + end) // 2
    
    if nums[mid] == mid:
      return mid
    elif nums[mid] < mid:
      start = mid + 1
    else:
      end = mid - 1
      
  return -1

n = int(input())
nums = list(map(int, input().split()))

start = 0
end = len(nums) - 1

result = binary_search(start, end)
if result == -1:
  print(-1)
else:
  print(result)
