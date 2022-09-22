# 수행시간 비교체험 - e 계산
# 2022.09.10 풀이 끝 -> 09.20 과제 마감 이후 공개
import time

def factorial(n):
	result = 1
	for i in range(1, n+1):
		result *= i
	return result

def compute_e_ver1(n):
	# code for O(n^2)-time version
	global p1_start, p1_end # 전역변수 지정 (함수 밖에서 호출하기 위함)
	p1_start = time.process_time() # 시작 시간

	sum = 1
	for i in range(1, n+1):
		deno = 1/factorial(i) #1/k!
		sum += deno
	
	print("오일러의 수: ", sum)
	p1_end = time.process_time() # 끝난 시간
	
	
def compute_e_ver2(n):
	# code for O(n)-time version
	global p2_start, p2_end # 전역변수 지정 (함수 밖에서 호출하기 위함)
	p2_start = time.process_time() # 시작 시간
	
	result = 1
	deno = 1
	for i in range(1, n+1):
		result *= i
		deno += 1/result

	print("오일러의 수: ", deno)
	p2_end = time.process_time() # 끝난 시간
	
	
# n 입력받음 (항의 개수)
n = int(input())

# compute_e_ver1 호출
compute_e_ver1(n)

# compute_e_ver2 호출
compute_e_ver2(n)

# 두 함수의 수행시간 출력
print(f'compute_e_ver1의 수행시간: {p1_end - p1_start:.6f}') # 소수점 6자리까지 출력
print(f'compute_e_ver2의 수행시간: {p2_end - p2_start:.6f}')
print(f'compute_e_ver1의 수행시간: {p1_end - p1_start}') # 그대로 출력
print(f'compute_e_ver2의 수행시간: {p2_end - p2_start}')