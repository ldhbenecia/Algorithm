import sys
input = sys.stdin.readline

n = int(input())
last_name = [input().strip()[0] for _ in range(n)]
set_last_name = set(last_name)

result = []
for i in set_last_name:
  if last_name.count(i) >= 5:
    result.append(i)
    
result.sort()
if result:
  print(''.join(result))
else:
  print('PREDAJA')