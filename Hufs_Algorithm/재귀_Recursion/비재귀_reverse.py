def reverse(A):
  n, i = len(A), 0
  while i < n/2:
    A[i], A[-i-1] = A[-i-1], A[i]
    i += 1
    
A = list(input())
reverse(A)
print(''.join(str(x) for x in A))