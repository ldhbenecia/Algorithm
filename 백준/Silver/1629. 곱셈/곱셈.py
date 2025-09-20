import sys

input = sys.stdin.readline


def multi(a, n):
    if n == 1:
        return a % c
    else:
        temp = multi(a, n // 2)
        if n % 2 == 0:
            return (temp * temp) % c
        else:
            return (temp * temp * a) % c


a, b, c = map(int, input().split())
print(multi(a, b))
