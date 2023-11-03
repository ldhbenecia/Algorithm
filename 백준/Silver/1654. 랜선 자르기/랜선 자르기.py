k, n = map(int, input().split())
cm_lst = []

for _ in range(k):
   lans = int(input())
   cm_lst.append(lans)

left, right = 1, max(cm_lst)
   
while left <= right:
   mid = (left + right) // 2
   cnt = 0
   
   for i in cm_lst:
      cnt += i // mid
      #print(i, cnt, mid, left, right)
   
   if cnt >= n:
      left = mid + 1
   else:
      right = mid - 1
      
print(right)