total_grade = 0
total_alpha = 0

alpha_list = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

for i in range(20):
  score = input().split()
  
  if score[2] == "P":
    continue
  
  total_grade += float(score[1])
  total_alpha += alpha_list[score[2]] * float(score[1])

#print(total_grade)
#print(total_alpha)

print(total_alpha/total_grade)
