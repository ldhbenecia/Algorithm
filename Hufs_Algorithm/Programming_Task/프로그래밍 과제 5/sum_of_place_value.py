def solve(L, S): # L: 자리수, S: 자리 값의 합
	# code here
	DP = [[0 for _ in range(S)] for _ in range(L)] # DP 테이블 생성

	if (S <= 9):
		for i in range(S):
			DP[0][i] = 1
	else:
		for i in range(9):
			DP[0][i] = 1
	
	for i in range(1, L):
			DP[i][0] = 1
			for j in range(1, S):
				if (j <= 9):
					DP[i][j] = DP[i-1][j] + DP[i][j-1]
				else:
					DP[i][j] = DP[i][j-1] + DP[i-1][j] - DP[i-1][j-10]

	return DP[L-1][S-1]
