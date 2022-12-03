# 예시 테케 입력: 4, 답: 2의 경우
# 0 1 2 3 으로 4*4 행렬이 만들어짐
# 거기서 퀸이 올 수 있는 자리를 리스트로 변환하면 x=[1,3,0,2](열 번호)) 하나가 나옴 
# 이것과 대칭한 것 하나까지 추가로 해서 2개, 나머지는 안됨

def Bounding(k, col): # check if the k-th queen can be placed at (k, col)
	# (k, col) 칸에 놓을 수 있으면 True, 아니면 False
	# 칸에 놓을 수 있는 경우 = 같은 행, 렬, 대각에 없을 때
	for r in range(1, k):
		if x[r] == col or abs(k-r) == abs(col-x[r]): # 절대값을 씌워주는 이유 -> 왼쪽으로 대각일수도 오른쪽으로 대각일수도 있는데 좌표가 음수로 바뀌므로 절대값 처리
			return False
	return True
	
def nQueens(k): # decide a valid x[k], x[k]의 값(열 번호)를 결정
	global sol  # sol: 전역 변수로 사용한다는 의미
	if k > n:
		sol += 1 # 해가 하나 발견되어 갯수 증가
		return
	for col in range(1, n+1):
		if Bounding(k, col): # if B(k, col) == True; (퀸 배치가 가능한 경우)
			x[k] = col # 그 행에 퀸 배치
			nQueens(k+1)

n = int(input())
x = [0]*(n+1) # 해를 기록
sol = 0 # 해의 개수를 기록
nQueens(1)
print(sol)
