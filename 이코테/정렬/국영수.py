n = int(input())

students = []
for _ in range(n):
  name, korean, english, mathmatics = input().split()
  students.append((name, korean, english, mathmatics))
  
students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in students:
  print(i[0])
  
# 정렬 조건
# 1. 국어 점수 내림차순
# 2. 국어 점수가 같다면 영어 점수 오름차순
# 3. 국어, 영어 점수가 같다면 수학 점수 내림차순
# 4. 국영수가 같으면 이름 사전 순