t = int(input())

for _ in range(t):
  string = input()
  score = 0
  sum_score = 0
  for i in range(len(string)):
    if string[i] == "O":
      score += 1
      sum_score += score
    else:
      score = 0

  print(sum_score)