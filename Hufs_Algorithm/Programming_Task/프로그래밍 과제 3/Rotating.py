# 정렬을 써야 하는 줄 알았지만 문제를 자세히 읽어본 결과
# 테스트케이스 1번에서 5 6 1 2 3 4가 주어지고 여기서 오름차순으로 정렬이 되려면 
# Rotating이 4번 되어야 한다는 것을 알게됨
# 마찬가지로 테스트케이스 2번도 1 3 5 6 7 9는 이미 오름차순이니까 Rotating할 값이 없으므로 0이 출력되는 것

# 분할정복 알고리즘 코드를 이용하여 리스트 A와 시작, 마지막 번째 위치를 가지고 함수 작성
# 이진탐색 활용

# O(logN)
def Rotating(A, start, last):
	if start == last: # 시작값과 마지막 값이 같다면 첫번째 값 출력
		return start # last 넣어도 똑같음
	
	mid = (start + last) // 2 # 분할정복을 해야하므로 가운데 mid 값 지정
	
	if A[mid] < A[last]: # 이진탐색 사용 
		return Rotating(A, start, mid) # A[0] ~ A[mid-1] 사이에 존재함
	else:
		return Rotating(A, mid + 1, last) # A[mid+1] ~ A[last] 사이에 존재함

A = list(map(int, input().split())) # 리스트 A 값 입력
k = len(A) - Rotating(A, 0, len(A)-1) # 함수 파라미터에 리스트 A, 시작 값 0, 마지막 값 len(A)-1

if len(A) == k: # 오름차순 일때
   k = 0
		
print(k)