n = int(input())

array = []

for i in range(n):
  age, name = map(str, input().split())
  age = int(age)
  array.append([age, name])
  
array.sort(key = lambda x : x[0])

for age, name in array:
  print(age, name)
