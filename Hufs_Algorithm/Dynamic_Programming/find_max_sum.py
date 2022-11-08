# 최대 구간 합

def find_max_sum(A):
  S = [0] * len(A)
  S[0] = A[0]
  
  for i in range(1, len(A)):
    S[i] = max(S[i-1] + A[i], A[i])
  return max(S)


A = [int(x) for x in input().split()]
solve = find_max_sum(A)
print(solve)