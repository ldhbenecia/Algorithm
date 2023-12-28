from itertools import combinations
n = [int(input()) for _ in range(9)]

result = list(combinations(n, 7))

for i in result:
  if sum(i) == 100:
    for j in i:
      print(j)