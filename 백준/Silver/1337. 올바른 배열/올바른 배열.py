n = int(input())
num = sorted([int(input()) for _ in range(n)])
result = []

for i in range(n):
  count = 0
  for j in range(num[i], num[i] + 5):
    if j not in num:
      count += 1
  result.append(count)
  
print(min(result))