n = int(input())

for _ in range(n):
  a, b = input().split()
  
  lst1 = sorted(a)
  lst2 = sorted(b)
  
  if lst1 == lst2:
    print("Possible")
  else:
    print("Impossible")