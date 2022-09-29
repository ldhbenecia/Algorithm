def QuickSelect(L, k): # O(n^2) - worst case, O(n) - best case, O(n) - average case
  A, M, B = [], [], [] # Small, Middle, Large sets to p
  p = L[0]  # pivot p is the first element of A

  for a in L: # O(n)
    if a < p:
      A.append(a)
    elif a == p:
      M.append(a)
    else:
      B.append(a)
      
  if len(A) >= k:
    return QuickSelect(A, k)
  elif len(A)+len(M) < k:
    return QuickSelect(B, k-len(A)-len(M))
  else:
    print(p)
    return p

n, k = map(int, input().split())
num_list = list(map(int,input().split()))
QuickSelect(num_list, k)