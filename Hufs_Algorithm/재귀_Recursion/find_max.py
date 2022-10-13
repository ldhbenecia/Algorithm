def find_max(A, n):
  if n == 1:
    return A[0]
  return max(find_max(A, n-1), A[-1])

A = tuple(map(int, input().split()))

print(find_max(A, len(A)))