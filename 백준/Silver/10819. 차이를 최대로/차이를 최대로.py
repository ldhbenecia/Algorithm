from itertools import permutations

def difference():
  max_sum = 0
  
  for i in permutations(nums):
    current = 0
    for j in range(n - 1):
      current += abs(i[j] - i[j + 1])
    if max_sum < current:
      max_sum = current

  return max_sum

n = int(input())
nums = list(map(int, input().split()))

print(difference())
