t = int(input())
lst = []
result = []

for i in range(t):
  instance = list(map(int, input().split()))
  instance.sort()

  result.append(instance[-3])
  
for j in result:
  print(j)