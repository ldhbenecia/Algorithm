n = int(input())
student = []

for i in range(n):
  name, score = input().split()
  student.append((name, score))
  
student.sort(key = lambda x: x[1])

for i in student:
  print(i[0], end = ' ')