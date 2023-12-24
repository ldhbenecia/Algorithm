# O(n)
# -10,000,000 < N < 10,000,000

n = int(input())
num = map(int, input().split())
m = int(input())
num_count = map(int, input().split())

dic = {}
result = []

for i in num:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1
    
for i in num_count:
  if i in dic:
    result.append(dic[i])
  else:
    result.append(0)

for i in result:
  print(i, end=" ")