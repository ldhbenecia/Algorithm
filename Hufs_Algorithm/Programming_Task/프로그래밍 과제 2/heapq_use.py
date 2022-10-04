'''
#10번까지 맞음
import heapq

def findkth(heap, k):
	kth_min = None
	for _ in range(k):
		kth_min = heapq.heappop(heap)
	return kth_min

A = list(map(int, input().split()))

M = []
M.append(A[0])

#첫 힙 생성
origin_heap = []
heapq.heappush(origin_heap, A[0])

for i in range(1, len(A)):
	heapq.heappush(origin_heap, A[i])
	#사본 힙 생성
	tmp_heap = origin_heap.copy()
	k = i//3 + 1 # 몇 번째로 작은 값인지
	kth = findkth(tmp_heap, k) # side 리스트 안의 요소 값 중에 k번째로 작은 값
	M.append(kth)

print(sum(M))
'''

import heapq

def findkth(heap, k):
	kth_min = None
	for _ in range(k):
		kth_min = heapq.heappop(heap)
	return kth_min

A = list(map(int, input().split()))

M = []
M.append(A[0])
kth, prev_k = A[0], 1

#첫 힙 생성
origin_heap = []
heapq.heappush(origin_heap, A[0])

for i in range(1, len(A)):
	heapq.heappush(origin_heap, A[i])
	tmp_heap = origin_heap.copy() # 사본 힙 생성
	k = i//3 + 1 # 몇 번째로 작은 값인지
	if(k == prev_k and A[i] > kth):
		M.append(kth)
	else:
		kth = findkth(tmp_heap, k) # k번째로 작은 값
		M.append(kth)
		prev_k = k

print(sum(M))