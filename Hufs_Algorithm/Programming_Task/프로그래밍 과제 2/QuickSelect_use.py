def QuickSelect(L, k): # 배점 8점까지만 정답 뜨는 코드 // 배점 26점
	A, M, B = [], [], [] # Small, Middle, Large sets to p
	p = L[0]  # pivot p is the first element of A
	for a in L:
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
		return p

num = list(map(int, input().split()))

A, side, M = [], [], []

for i in num:
	A.append(i)

M.append(A[0])
side.append(A[0])

for i in range(1, len(A)):
	side.append(A[i])
	k = i//3 + 1 # 몇 번째로 작은 값인지
	kth = QuickSelect(side, k) # side 리스트 안의 요소 값 중에 k번째로 작은 값
	M.append(kth)

print(sum(M))