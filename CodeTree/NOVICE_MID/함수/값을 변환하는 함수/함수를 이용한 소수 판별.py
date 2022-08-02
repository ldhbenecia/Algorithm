a, b = map(int, input().split())

def is_prime_number(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


sum = 0
for i in range(a, b + 1):
    if is_prime_number(i):
        sum += i

print(sum)