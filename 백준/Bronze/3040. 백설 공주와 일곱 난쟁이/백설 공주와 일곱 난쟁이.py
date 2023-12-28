n = [int(input()) for _ in range(9)]

for i in range(8):
  for j in range(i + 1, 9):
    if sum(n) - n[i] - n[j] == 100:
      n[i], n[j] = 0, 0

result = [i for i in n if i != 0]

for i in result:
  print(i)