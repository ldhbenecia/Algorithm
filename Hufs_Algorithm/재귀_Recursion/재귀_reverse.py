def reverse(L, a):
  n = len(L)
  if a < n/2:
    L[a], L[-a-1] = L[-a-1], L[a]
    reverse(L, a+1)
    
L = list(input())
reverse(L, 0)
print(''.join(str(x) for x in L))