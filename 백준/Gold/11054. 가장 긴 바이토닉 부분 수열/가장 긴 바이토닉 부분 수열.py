n = int(input())
nums = list(map(int, input().split()))
increase = [1] * n
decrease = [1] * n
bitonic = [0] * n

for i in range(1, n):
  for j in range(i):
    if nums[i] > nums[j]:
      increase[i] = max(increase[i], increase[j] + 1)
  
nums.reverse()
for i in range(1, n):
  for j in range(i):
    if nums[i] > nums[j]:
      decrease[i] = max(decrease[i], decrease[j] + 1)
decrease.reverse()
      
for i in range(n):
  bitonic[i] = increase[i] + decrease[i]
  
print(max(bitonic) - 1)
