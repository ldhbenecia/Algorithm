n = int(input())
quantity = sorted(list(map(int, input().split())))
total = quantity[-1]

for i in range(n - 1):
  total += quantity[i] / 2
  
print(total)