import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
  x = int(input())
  
  if x > 0:
    heapq.heappush(heap, -x)
  elif x == 0:
    if heap:
      print(abs(heapq.heappop(heap)))
    else:
      print(0)
