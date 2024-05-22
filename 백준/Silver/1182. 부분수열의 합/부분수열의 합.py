import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

for r in range(1, n + 1):
  for comb in combinations(nums, r):
    if sum(comb) == s:
      count += 1

print(count)
