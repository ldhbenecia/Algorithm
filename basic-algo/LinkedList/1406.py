str_list = list(input())
str_list2 = []
m = int(input())

for i in range(m):
  commend = list(input().split())
   
  if commend[0] == "P":
    str_list.append(commend[1])
  
  elif commend[0] == "L":
    if str_list:
      str_list2.append(str_list.pop())
  
  elif commend[0] == "D":
    if str_list2:
      str_list.append(str_list2.pop())
  
  elif commend[0] == "B":
    if str_list:
      str_list.pop()
    
print("".join(str_list + list(reversed(str_list2))))