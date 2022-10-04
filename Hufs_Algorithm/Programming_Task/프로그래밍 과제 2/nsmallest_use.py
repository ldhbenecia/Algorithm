# 9번까지만 통과
from heapq import nsmallest

A = list(map(int, input().split()))

side, M = [], []

M.append(A[0])
side.append(A[0])

for i in range(1, len(A)):
	side.append(A[i])
	k = i//3 + 1 # 몇 번째로 작은 값인지
	kth = nsmallest(k, side)[-1] # side 리스트 안의 요소 값 중에 k번째로 작은 값
	M.append(kth)

print(sum(M))