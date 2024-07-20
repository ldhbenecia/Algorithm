def power(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (power(a, b // 2, c) ** 2) % c
    else:
        return ((power(a, b // 2, c) ** 2) * a) % c

a, b, c = map(int, input().split())
print(power(a, b, c))

# 3^100 == 3^50 * 3^50 == 3^25 * 3^25 * 3^25 * 3^25
# 위와 같이 제곱할 횟수를 2로 나누면서 분할정복이 가능해짐
# 지수법칙에 해당하는 제곱할 횟수가 짝수일 경우, 홀수일 경우에 대한 식 구현 필요
