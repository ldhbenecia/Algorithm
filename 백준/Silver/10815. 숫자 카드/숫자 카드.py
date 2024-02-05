n = int(input())
nums = map(int, input().split())
m = int(input())
find_nums = map(int, input().split())

dic = {}

for i in nums:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1
    
for i in find_nums:
  if i in dic:
    print(1, end=" ")
  else:
    print(0, end=" ")