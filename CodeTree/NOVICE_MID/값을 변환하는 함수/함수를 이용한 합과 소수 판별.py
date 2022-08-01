a, b = map(int, input().split())


def is_prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True

def degit_sum_number(n):
    sum = (n // 100) + ((n // 10) % 10) + (n % 10)
    if sum % 2 == 0:
        return True
    return False

def judge_num(n):
    if is_prime_number(n) and degit_sum_number(n):
        return True
    return False

cnt = 0
for i in range(a, b + 1):
    if judge_num(i):
        cnt += 1

print(cnt)
