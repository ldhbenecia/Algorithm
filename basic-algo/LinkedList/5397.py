t = int(input())

for i in range(t):
  password = list(input())
  
  left = []
  right = []
  
  for i in password:
    if i == ">":
      if right:
        left.append(right.pop())
      
    elif i == "<":
      if left:
        right.append(left.pop())
      
    elif i == "-":
      if left:
        left.pop()
        
    else: # 문자가 추가되었을때
      left.append(i)
      
  print("".join(left) + "".join(reversed(right)))