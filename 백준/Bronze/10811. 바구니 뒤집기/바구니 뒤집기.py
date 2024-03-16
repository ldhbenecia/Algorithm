n, m = map(int, input().split())

lst = [i for i in range(1, n + 1)]

for _ in range(m):
  i, j = map(int, input().split())
  temp = lst[i-1:j]
  temp.reverse()
  lst[i-1:j] = temp
  
for i in range(n):
  print(lst[i], end = " ")