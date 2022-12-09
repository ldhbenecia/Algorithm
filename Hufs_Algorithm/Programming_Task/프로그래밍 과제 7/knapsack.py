def knapsack(i, size):
	global MaxProfit # 현재까지 가장 큰 가치 값
	
	if i >= N or size <= 0:
		return
	
	s, p = 0, 0
	
	for k in range(i):
		if x[k] == 1:
			s += S[k]
			p += P[k]
	
	# x[i] = 1 선택하는 경우
	if S[i] <= size:
		B = frac_knapsack(i+1, size-S[i]) # B(i-1) 초기값을 아예 B로 잡아버림
		if p + P[i] + B > MaxProfit: # 예상 이익이 MP보다 클 떄
			# Update MP
			if p + P[i] > MaxProfit:
				MaxProfit = p + P[i]
			x[i] = 1
			knapsack(i+1, size-S[i])
	
	# x[i] = 0 선택하는 경우
	B = frac_knapsack(i+1, size)
	if p + B > MaxProfit: # 예상 이익이 MP보다 클 때
		x[i] = 0
		knapsack(i+1, size)
	
def frac_knapsack(i, size):
	if size <= 0:
		return 0
	
	s,p = 0,0
	
	for k in range(i, N):
		if s + S[k] <= size:
			p += P[k]
			s += S[k]
		else:
			p += (size-s) * (P[k]/S[k])
			s = size
			break
	return p

	
K = int(input())
N = int(input())
S = list(map(int, input().split()))
P = list(map(int, input().split()))
x = [0] * N
gs = [0] * N

for i in range(N): # 가성비 값 넣기
	gs[i] = P[i] / S[i]
	
gs.sort(reverse=True) #가성비 내림차순 정렬
for i in range(N):
	for j in range(i,N):
		if (P[j]/S[j]) == gs[i]: # S,P 정렬
			S[i],S[j] = S[j],S[i]
			P[i],P[j] = P[j],P[i]
			break

MaxProfit = 0
knapsack(0, K)
print(MaxProfit)