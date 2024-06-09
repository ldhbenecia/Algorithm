import sys
input = sys.stdin.readline

# (1 ≤ N ≤ 4,000,000)
# 소수 에라토스테네스의 체 사용해서 추출
def search(n):
  # 0과 1은 소수가 아님
  primes[0] = primes[1] = False
  
  for i in range(2, int(n**0.5) + 1):
    # True인 값들 소수 판별
    if primes[i]:
      for j in range(i * i, n + 1, i): # 해당 i의 배수들을 False로 설정
        primes[j] = False

n = int(input())
primes = [True for _ in range(n + 1)] # 0부터 n까지 전부 소수 True로 초기화

search(n)

prime_nums = []
for i in range(len(primes)):
  if primes[i]:
    prime_nums.append(i)

start, end, count = 0, 0, 0
while start < len(prime_nums) and end < len(prime_nums):
  temp = sum(prime_nums[start:end+1])
  if temp == n:
    count += 1
    end += 1
  elif temp < n:
    end += 1
  elif temp > n:
    start += 1
  
print(count)