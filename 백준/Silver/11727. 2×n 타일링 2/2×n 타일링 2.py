n = int(input())

lst = [0, 1, 3, 5] # 0 1 2 5

for i in range(4, n + 1):
   lst.append(lst[i-1] + (2 * lst[i-2]))
   
print(lst[n] % 10007)