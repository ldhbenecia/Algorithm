def insertion_sort(A):
  n = len(A)
  for i in range(1, n):
    x = A[i]
    
    j = binary_search(A, 0, i-1, x)
    k = i - 1
    while k >= j:
      A[k], A[k+1] = A[k+1], A[k]
      k -= 1
    A[j] = x
    
def binary_search(A, left, right , x):
  if left == right:
    if A[left] <= x: return left + 1
    return left
  m = (left + right) // 2
    
  if A[m] > x:
    return binary_search(A, left, m, x)
  else:
    return binary_search(A, m+1, right, x)
  
A = [int(x) for x in input().split()]
insertion_sort(A)
print(A)