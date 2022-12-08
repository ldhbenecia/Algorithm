def quick_sort(A, first, last): # in-place, unstable
	if first >= last: return
	left, right = first + 1, last
	pivot = A[first] # 첫 번째 값 pivot
	while left <= right: # pivot보다 작은 값은 왼쪽, 큰 값은 오른쪽
		while left <= last and A[left] < pivot:
			left += 1
		while right > first and A[right] > pivot:
			right -= 1
		if left <= right: # swap A[left] and A[right]
			A[left], A[right] = A[right], A[left]
			left += 1
			right -= 1
			
	A[first], A[right] = A[right], A[first] # pivot을 제 위치로 보냄 (Pivot과 first를 바꾸기 위함)
	
	quick_sort(A, first, right - 1) # pivot보다 작은 것들을 재귀 정렬
	quick_sort(A, right + 1, last) # pivot보다 큰 값들을 재귀 정렬
