n = int(input())
word = [input() for _ in range(n)]
count = n

for i in word:
  for j in range(len(i)-1):
    if i[j] == i[j + 1]:
      continue
    elif i[j] in i[j + 1:]:
      count -= 1
      break

print(count)
