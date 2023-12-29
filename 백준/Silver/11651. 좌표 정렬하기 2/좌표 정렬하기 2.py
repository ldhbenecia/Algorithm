n = int(input())

result = []

for i in range(n):
  x, y = map(int, input().split())
  result.append([y, x])
  
result.sort()

for x, y in result:
  print(y, x)
