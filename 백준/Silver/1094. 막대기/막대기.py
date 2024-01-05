x = int(input())
cnt = 0
stick = 64

while x > 0:
  if stick > x:
    stick //= 2
  else:
    cnt += 1
    x -= stick
    
print(cnt)