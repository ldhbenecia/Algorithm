n = list(map(int,input().split()))

sorted_list = sorted(n)
reverse_sorted_list = sorted(n, reverse=True)

if n == sorted_list:
  print("ascending")

elif n == reverse_sorted_list:
  print("descending")
  
else:
  print("mixed")