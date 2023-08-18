
count = 0
result = []

for i in range(1, 10 + 1):
  off, on = map(int, input().split())
  
  if i == 1:
    count += on
    result.append(count)
  else:
    count -= off
    count += on
    result.append(count)
    

print(max(result))