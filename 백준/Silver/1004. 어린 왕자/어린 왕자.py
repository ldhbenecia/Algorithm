import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  count = 0
  for _ in range(n):
    cx, cy, r = map(int, input().split())
    
    is_start_point_inner_circle = ((x1 - cx)**2 + (y1 - cy)**2) <= r**2
    is_end_point_inner_circle = ((x2 - cx)**2 + (y2 - cy)**2) <= r**2
    
    if is_start_point_inner_circle is True and is_end_point_inner_circle is False:
      count += 1
    elif is_start_point_inner_circle is False and is_end_point_inner_circle is True:
      count += 1

  print(count)
