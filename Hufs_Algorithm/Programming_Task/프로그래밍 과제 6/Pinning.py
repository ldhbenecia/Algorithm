# 강의실 배정 문제와 거의 일치한다.
# 강의실 배정 문제의 경우 리스트 2개를 써서 끝나는 시간을 기준으로 오름차순 정렬을 하였다.
# 이에 이 문제도 막대의 끝점을 기준으로 오름차순 정렬을 하였는데, 
# 막대의 끝점을 기준으로 오름차순을 한만큼 둘이 묶여야 하므로 tuple로 값을 저장받았다.
# 2차원 리스트를 정렬하는 방법 중 lambda 방식을 사용하였는데 x:x[1]을 통해 끝점부터 정렬이 가능하다.
# 끝점을 기준으로 다음에는 시점을 본다.
# stick 이라는 변수에 제일 첫 막대의 끝점을 저장한다.
# 그리고 반복문을 돌며 끝점이 그 다음에 올 막대의 시점 값보다 작다면? -> 다음 막대의 시점이 첫 막대의 끝점보다 크다면? -> 이 핀 하나로 꽂을 수 없음 고로 count += 1
# 핀이 하나 추가되었으므로 기준이되는 stick의 값은 저 경우의 끝점으로 변경

# 시간복잡도는 2차원 리스트를 정렬할 때 사용한 lambda의 영향으로 O(nlogn)
# O(n), O(nlogn)이므로 O(nlogn)

def pin(L, n):
	count = 1 
	stick = L[0][1]
	for i in range(1, n): #O(n)
		if stick < L[i][0]:
			count += 1
			stick = L[i][1]
	return count

n = int(input())
L = [tuple(map(int, input().split())) for _ in range(n)]
	
L.sort(key=lambda x:x[1]) # 강의실 배정 문제대로 끝점을 기준으로 오름차순 정렬 O(nlogn)
cnt = pin(L, n)
print(cnt)