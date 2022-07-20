def max_sum(A):
  # 최대 구간 합 리턴
  
  ''' # 테스트케이스 2개 에러남
  # 부분합 수열: O(n^2)
  P = [0] * len(A)
  P[0] = A[0]
  for i in range(1, len(A)):
    P[i] = P[i-1] + A[i]
    
  result = 0
    
  for i in range(1, len(A)):
    for j in range(1, i+1):
      result = max(result, P[i] - P[j-1])
  return result
  '''

  # 동적 계획법: O(n)
  P = [0] * len(A)
  P[0] = A[0]
  for i in range(1, len(A)):
    P[i] = max(0, P[i-1]) + A[i]
  return max(P)


A = [int(x) for x in input().split()]
sol = max_sum(A)
print(sol)