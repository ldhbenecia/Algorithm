lst = []

for i in range(5):
  n = int(input())
  lst.append(n)
  
avg = sum(lst) // 5
mid = len(lst) / 2

lst.sort()
midValue = lst[int(mid)]

print(avg)
print(midValue)