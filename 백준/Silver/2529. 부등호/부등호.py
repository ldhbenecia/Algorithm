import sys
input = sys.stdin.readline

def check_sign(a, b, op):
  if op == '<':
    return a < b
  else:
    return a > b

def dfs(idx, num):
  if idx == k + 1:
    lst.append(num)
    return
  
  for i in range(10):
    if not check[i]:
      if idx == 0 or check_sign(num[-1], str(i), sign[idx - 1]):
        check[i] = 1
        dfs(idx + 1, num + str(i))
        check[i] = 0

k = int(input())
sign = list(input().split())
check = [0] * 10
lst = []
dfs(0, '')

print(lst[-1])
print(lst[0])
