# 테스트케이스 1번을 예시로 두자면 W = 12, 그리고 입력된 단어의 개수는 5개이다.
# 0 ape - 3 (글자 수)
# 1 eats - 4 (글자 수)
# 2 apple - 5 (글자 수)
# 3 cider - 5 (글자 수)
# 4 a - 1 (글자 수)
# 5 lots. - 4 (글자 수)
# 5개이므로 5*5 2차원 리스트를 만들어서 계산을 진행한다.
# 각각 [0][0], [1][1], [2][2], [3][3], [4][4], [5][5] 값의 경우 
# [0][0]은 W(12) - ape의 글자수 3개를 하면 남는 개수는 9개이므로 81이 들어간다.
# 이 방식으로 [1][1] = 64, [2][2] = 49, [3][3] = 49, [4][4] = 121, [5][5] = 64가 들어가며
# [0][1] 같은 경우는 0과 1 ape, eats의 글자수의 합은 7이고 이 두 단어를 합치면 공백 1개가 들어가게 되어 8칸을 차지한다. W(12)에서 8을 빼면 4가 남고 4의 3제곱을 하면 4*4*4 = 64가 되어 들어가게 된다.
# 이와 같은 방식으로 DP 테이블을 만들어서 코드를 작성하였다.

W = int(input()) # 페이지 폭
words = input().split()
# code below
# 시간 복잡도 (n^2) - 이중 for문만 사용

n = len(words)
DP = [[float('inf')]*n for _ in range(n)] # DP Table 생성 시작
minDP = [float('inf')]*n # 결과값 출력할 것
	

for i in range(n):
	DP[i][i] = W - len(words[i]) # 위에 말한 알고리즘대로 W에서 빼서 우선 넣어줌
	for j in range(i+1, n):
			DP[i][j] = DP[i][j-1] - len(words[j]) - 1

# 글자 수와 공백이 폭을 초과하면 inf 값을 넣어줌
for i in range(n):
	for j in range(i, n):
		if(DP[i][j] < 0):
			DP[i][j] = float('inf')
		else:
			DP[i][j] = DP[i][j]**3 # penalty 공식 사용
	
# 최소 penalty 찾는 식, i~len 사이의 j 값을 확인
for i in range(n-1, -1, -1):
	minDP[i] = DP[i][n-1]
	for j in range(n-1, i, -1):
		if DP[i][j-1] == float('inf'):
			continue
		if (minDP[i] > minDP[j] + DP[i][j-1]):
			minDP[i] = minDP[j] + DP[i][j-1]
			
print(minDP[0])
