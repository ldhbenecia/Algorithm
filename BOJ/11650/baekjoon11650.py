n = int(input())

arr = []

for i in range(n):
  a, b = map(int, input().split())
  arr.append([a, b])

arr_sort = sorted(arr)

for i in range(n):
  print(arr_sort[i][0], arr_sort[i][1])