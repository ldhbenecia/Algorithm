n = int(input())
num = list(map(int, input().split()))
m = int(input())
find_num = list(map(int, input().split()))

dic = {}

for i in find_num:
  dic[i] = 0

for i in num:
  if i in dic:
    dic[i] = 1
    
for i in dic:
  print(dic[i], end = " ")