n = int(input())
number = list(map(int,input().split()))
prime_cnt = 0

if 1 in number:
    number.remove(1)

# 소수 판별 함수
def prime(x):
    if x == 2:
        return True # 소수
    for i in range(2, x):
        if x % i == 0:
            return False # 소수 아님
    return True # 소수

for i in number:
    if prime(i):
        prime_cnt += 1

print(prime_cnt)