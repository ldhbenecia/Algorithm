import sys
import heapq
input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
   x = int(input())
   
   if x > 0:
      heapq.heappush(lst, -x)
   elif x == 0:
      if lst:
         print(-1 * heapq.heappop(lst))
      else:
         print(0)
         