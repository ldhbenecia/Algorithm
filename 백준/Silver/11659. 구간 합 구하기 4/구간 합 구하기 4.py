n, m = map(int, input().split())
num = list(map(int, input().split()))

lst = [0]
sum_of_num = 0

for i in range(n):
  sum_of_num += num[i]
  lst.append(sum_of_num)

#print(lst) # 0 5 9 12 14 15

for _ in range(m):
  start, end = map(int, input().split()) 
  print(lst[end] - lst[start-1])
  
# 1 3이 들어오면 12 => 12 - 0 = 12
# 2 4가 들어오면 9 => 14 - 5 = 9
