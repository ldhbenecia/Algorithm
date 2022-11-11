n  = int(input())

coins = [100, 50, 10, 1]
cnt = 0

for i in coins:
  cnt += n // i
  n %= i
  
print(cnt)