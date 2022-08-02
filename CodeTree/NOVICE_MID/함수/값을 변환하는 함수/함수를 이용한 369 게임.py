a, b = map(int, input().split())

def condition(n):
    # 3, 6, 9 중 하나가 들어가 있는지
    while n > 0:
        if n % 10 == 3 or n % 10 == 6 or n % 10 == 9:
            return True
        n //= 10
    return False

def condition2(n):
    # 3, 6, 9 중 하나가 들어가 있거나 그 숫자 자체가 3의 배수인 숫자 개수
    return condition(n) or (n % 3 == 0)


cnt = 0
for i in range(a, b + 1):
    if condition2(i):
        cnt += 1

print(cnt)