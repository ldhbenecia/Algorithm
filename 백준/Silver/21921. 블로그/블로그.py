import sys
input = sys.stdin.readline

n, x = map(int, input().split())
visited_count = list(map(int, input().split()))

if max(visited_count) == 0:
  print('SAD')
else:
  value = sum(visited_count[:x])
  max_value = value
  max_period = 1
  
  for i in range(x, n):
    value += visited_count[i]
    value -= visited_count[i - x]
    
    if value > max_value:
      max_value = value
      max_period = 1
    elif value == max_value:
      max_period += 1
      
  print(max_value)
  print(max_period)
