'''
m, n = map(int,input().split())

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in range(m, n+1):
    if is_prime_number(i):
        print(i)

// m부터 n까지의 값을 하나 하나 확인하려고 하니 시간 초과 뜸
'''

m, n = map(int,input().split())

def is_prime_list(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
    return True

for i in range(m, n+1):
    if is_prime_list(i):
        print(i)

# 시간초과가 떴으므로 제곱근까지만 확인해주면 시간을 줄일 수 있음
# 에라토스테네스의 체 원리 이용
# import math를 통해 sqrt(루트)를 사용해주어도 되지만
# import math를 선언하지않고 **0.5을 통해 제곱근을 계산