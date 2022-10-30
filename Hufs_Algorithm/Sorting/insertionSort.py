def insertion_sort(A, n): # A[0] ~ A[n-1]까지 insertion sort 
  for i in range(1, n): # round i에 i번째 작은 수를 찾음
    j=i-1
    while j >= 0 and A[j] > A[j+1]:
      A[j], A[j+1] = A[j+1], A[j] 
      j=j-1