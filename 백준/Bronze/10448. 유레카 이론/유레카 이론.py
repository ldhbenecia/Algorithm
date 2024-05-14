trangle = [i * (i + 1) // 2 for i in range(1, 45)]
eureka = [0] * 1001

for i in trangle:
  for j in trangle:
    for k in trangle:
      num = i + j + k
      if num <= 1000:
        eureka[num] = 1

t = int(input())
for _ in range(t):
  print(eureka[int(input())])
