n = int(input())
array = [[0] * 101 for _ in range(101)]

for _ in range(n):
  x, y = map(int, input().split())
  for i in range(10):
    for j in range(10):
      array[x+i][y+j] = 1
      
result = 0
for i in array:
  result += sum(i)
  
print(result)