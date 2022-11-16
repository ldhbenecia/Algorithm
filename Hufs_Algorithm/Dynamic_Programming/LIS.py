def print_IS(seq, x):
  for i in range(len(seq)):
    if x[i]: 
      print(seq[i], end="")
    else:
      print("_", end="")
    print()

def LIS_DP(seq):
	# code here
	x = [0] * len(seq)
	DP = [0] * len(seq) # DP table
	
	DP[0] = 1;
	for i in range(1, len(seq)):
		DP[i] = 1
		for j in range(i-1, -1, -1):
			if seq[i] > seq[j]:
				DP[i] = max(DP[i], DP[j] + 1)
	return max(DP), x

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis, x = LIS_DP(seq)
print(lis)