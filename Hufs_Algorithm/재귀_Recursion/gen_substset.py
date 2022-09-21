def gen_subsets(k):
  if k == n:
    print(S)
  else:
    S.append(k)
    gen_subsets(k+1)
    S.pop()
    gen_subsets(k+1)
    
S = []
n = int(input())
gen_subsets(0)