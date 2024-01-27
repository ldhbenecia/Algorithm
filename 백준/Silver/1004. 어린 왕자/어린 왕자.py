import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  x1, y1, x2, y2 = map(int, input().split())
  n = int(input())
  count = 0
  for _ in range(n):
    cx, cy, r = map(int, input().split())
    
    distance_start = (x1 - cx)**2 + (y1 - cy)**2
    distance_end = (x2 - cx)**2 + (y2 - cy)**2
    
    if (distance_start < r**2 and distance_end > r**2) or (distance_start > r**2 and distance_end < r**2):
      count += 1

  print(count)
