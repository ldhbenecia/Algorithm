import time, random

def prefixSum1(X, n): # O(n^2)
  global p1_start, p1_end # 전역변수 지정 (함수 밖에서 호출하기 위함)
  p1_start = time.process_time() # 시작 시간
  S = [0] * n
  for i in range(n):
    S[i] = 0
    for j in range(i+1):
      S[i] += X[j]
  p1_end = time.process_time() # 끝난 시간
	
def prefixSum2(X, n): # O(n)
  global p2_start, p2_end # 전역변수 지정 (함수 밖에서 호출하기 위함)
  p2_start = time.process_time() # 시작 시간
  S = [0] * n
  S[0] = X[0]
  for i in range(n):
    S[i] = S[i-1] + X[i]
  p2_end = time.process_time() # 끝난 시간


random.seed()		# random 함수 초기화

# n 입력받음
n = int(input())

# 리스트 X를 randint를 호출하여 n개의 랜덤한 숫자로 채움
X = []
for i in range(n):
  X.append(random.randint(-999, 999))

# prefixSum1 호출
prefixSum1(X, n)

# prefixSum2 호출
prefixSum2(X, n)

# 두 함수의 수행시간 출력
print(f'PrefixSum1: {p1_end - p1_start:.6f}') # 소수점 6자리까지 출력
print(f'PrefixSum2: {p2_end - p2_start:.6f}')
print(f'PrefixSum1: {p1_end - p1_start}') # 그대로 출력
print(f'PrefixSum2: {p2_end - p2_start}')