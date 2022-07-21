def max_sum(A, left, right):
  # A[left], ..., A[right] 중 최대 구간 합 리턴
  if left == right:
    return A[left]
  
  mid = (left + right) // 2
  sum = 0
  
  i = mid
  # 중간에 걸친 경우, 왼쪽 최대합
  while (i >= left):
    sum += A[i]
    left = max(left, sum)
    i -= 1
    
  # 중간에 걸친 경우, 오른쪽 최대합
  sum = 0
  j = mid + 1
  while (j <= right):
    sum += A[j]
    right = max(right, sum)
    j += 1
    
  # 걸치지 않고 양분된 구간 내에 속하는 경우
  single = max(max_sum(A, left, mid), max_sum(A, mid + 1, right))
  
  # 중간에 걸친 경우와 걸치지 않은 경우 중 높은 값을 반환
  return max(left + right, single)
   
   

A = [int(x) for x in input().split()]
sol = max_sum(A, 0, len(A)-1)
print(sol)