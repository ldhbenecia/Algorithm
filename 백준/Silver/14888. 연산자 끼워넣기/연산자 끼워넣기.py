n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_value = -1000000000
min_value = 1000000000
  
def dfs(idx, total, add, sub, mul, div):
  global max_value, min_value
  
  if idx == n:
    max_value = max(max_value, total)
    min_value = min(min_value, total)
    return
  
  if add:
    dfs(idx + 1, total + nums[idx], add - 1, sub, mul, div)
  if sub:
    dfs(idx + 1, total - nums[idx], add, sub - 1, mul, div)
  if mul:
    dfs(idx + 1, total * nums[idx], add, sub, mul - 1, div)
  if div:
    dfs(idx + 1, int(total / nums[idx]), add, sub, mul, div - 1)
  
dfs(1, nums[0], add, sub, mul, div)

print(max_value)
print(min_value)