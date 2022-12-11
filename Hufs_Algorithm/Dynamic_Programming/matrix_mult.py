import math

# 행렬의 곱셈을 계산하는 것이 아니라 행렬 위치에 들어가 있는 비용값을 계산하는 것이며,
# 행렬은 M_0부터 시작하므로 범위 설정에 유의하여야 함.
# 행렬 곱셈 2 5 5 10 이런 식의 유튜브 강의는 
# DP[i][i]는 0이고 본인 자신과 곱셈을 할 수 없어서 1부터 시작하는데 이 문제는 0부터 하여야 함

def matrix_mult():
	for l in range(1, n):
		for i in range(0, n-l):
			j = i + l
			DP[i][j] = math.inf # math module에서 제공하는 매우 큰 정수
			for k in range(i, j):
				cost = DP[i][k] + DP[k+1][j] + P[i]*P[k+1]*P[j+1]
				if cost < DP[i][j]: # cost에 최소값이 저장되어있음
					DP[i][j] = cost # DP[i][j]에 최소값 저장
	return DP[0][n-1]


n = int(input()) # n = 행렬 갯수, M_0부터 행렬시작임을 주의!
P = [int(x) for x in input().split()] # M_i = p_i x p_{i+1}
DP = [[0]*n for _ in range(n)] # 비용을 저장할 2차원 리스트 C 초기화
min_cost = matrix_mult()
print(min_cost)