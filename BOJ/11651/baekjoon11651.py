n = int(input())

array = []

for i in range(n):
  x, y = map(int, input().split())
  array.append([y, x])
  
array.sort()

for y, x in array:
  print(x, y)