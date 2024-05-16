n = int(input())
price = [int(input()) for _ in range(n)]
price.sort(reverse=True)

total = 0
for i in range(0, n, 3):
  group = price[i:i+3]
  cheap = group[-1]
  
  if len(group) == 3:
    total += sum(group) - cheap
  else:
    total += sum(group)

print(total)
