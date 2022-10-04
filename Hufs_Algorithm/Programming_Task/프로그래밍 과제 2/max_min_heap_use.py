import heapq # O(logn)

# 최소힙, 최대힙 둘 다 사용
def findkth(A):
	result = []
	max_heap, min_heap = [], [] # max, min heap
	
	for i in range(len(A)):
		k = i//3+1 # k 범위 설정
		
		# max_heap이 비어있거나, max_heap의 루트값보다 i값이 작거나 같다면, -i 삽입
		if not max_heap or -max_heap[0] >= A[i]:
			heapq.heappush(max_heap, -A[i])
			
		# 그 외에는 min_heap에 i 삽입
		else:
			heapq.heappush(min_heap, A[i])
			
		 # min_heap의 루트노드를 k번째 작은 수로 만들기 위하여 min_heap의 크기를 k개로 유지
		if len(max_heap) > k:
			heapq.heappush(min_heap, -heapq.heappop(max_heap))
		elif len(max_heap) < k and min_heap:
			heapq.heappush(max_heap, -heapq.heappop(min_heap))
			
		result.append(-max_heap[0]) # 루트 노드 == k번째 작은수
		
	return result

A = list(map(int, input().split())) # A 리스트 입력
M = findkth(A) # k번째 작은수 찾는 함수 호출하여 result 리스트를 M으로 반환
print(sum(M)) # M값 합