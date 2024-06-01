n = int(input())

students = []
for _ in range(n):
  name, korean, english, mathmatics = input().split()
  students.append((name, korean, english, mathmatics))
  
students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in students:
  print(i[0])
