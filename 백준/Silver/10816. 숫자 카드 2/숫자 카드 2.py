n = int(input())
num = list(map(int, input().split()))

m = int(input())
find_num = list(map(int, input().split()))

dic = {}

for i in num:
  if i not in dic:
    dic[i] = 1
  else:
    dic[i] += 1

for i in find_num:
  if i in dic:
    print(dic[i], end = " ")
  else:
    print(0, end = " ")