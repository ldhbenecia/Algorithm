a, b = map(int, input().split())
cnt = 1

while (a < b):
  if b % 2 == 0:
    b //= 2
  else:
    if (int(str(b)[-1]) == 1):
      b = int(str(b)[:-1])
    else:
      break
    
  cnt += 1
  
if (a == b):
  print(cnt)
else:
  print(-1)
