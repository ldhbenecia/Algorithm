def print_subset(x):
  	print([A[i] for i in range(len(x)) if x[i]])

def subset_sum(k):
	global subset_sum_cnt
	
	v_sum = sum(A[i] * x[i] for i in range(len(x)))
	
	if k == len(A):
		if v_sum == S:
			subset_sum_cnt += 1 # 개수가 추가될때마다 +1씩 해줌
			print_subset(x)
		if sum(x) == 0 and subset_sum_cnt == 0: # 최종합이 0, 개수도 아예 추가되지 않은 경우
			print([])

	else:
		# code for x[k] = 1 and x[k] = 0
		# 선택하는 경우
		if v_sum + A[k] <= S:
			x[k] = 1
			subset_sum(k+1)
		# 선택하지 않은 경우
		x[k] = 0
		subset_sum(k+1)

subset_sum_cnt = 0
A = list(set(int(x) for x in input().split()))
A.sort()
S = int(input()) 
x = [0]*len(A)
subset_sum(0)