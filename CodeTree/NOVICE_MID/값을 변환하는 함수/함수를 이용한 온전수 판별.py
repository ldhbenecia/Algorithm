a, b = map(int, input().split())

def is_onjunsu(n):
    if n % 2 == 0:
        return False
    elif n % 10 == 5:
        return False
    elif (n % 3 == 0) and (n % 9 != 0):
        return False
    else:
        return True


cnt = 0
for i in range(a, b + 1):
    if is_onjunsu(i):
        cnt += 1
print(cnt)

