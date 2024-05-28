n = int(input())
coin = sorted(list(map(int, input().split())))

print(coin)
target = 1
for i in coin:
  if target < i:
    break
  target += i

print(target)

"""
5
3 2 1 1 9

8
"""
