def binary_search(A, K):
  l, r = 0, len(A)
  
  while l - r >= 0:
    m = (l+r) // 2
    if A[m] > K:
      r = m -1
    elif A[m] < K:
      l = m + 1
    else:
      return m
    
# Slicing을 사용하지 않아 메모리 낭비가 적고, 비재귀적이라 재귀호출의 부담이 없는
# 가장 이상적인 이진 탐색 코드