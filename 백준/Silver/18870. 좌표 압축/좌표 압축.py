n = int(input())
location = list((map(int, input().split())))
setLocation = sorted(set(location))

dic = {}

for i in range(len(setLocation)):
  dic[setLocation[i]] = i

for i in location:
  print(dic[i], end = " ")
  