n = int(input())
num = map(int, input().split())
m = int(input())
find_num = map(int, input().split())

dic = {}

for i in num:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1
    
result = []
for i in find_num:
  if i in dic:
    result.append(dic[i])
  else:
    result.append(0)
    
print(*result)