m = int(input())
n = int(input())

prime = []

for i in range(m, n+1):
    if i != 1:
        check = True
        for j in range(2, i):
            if i % j == 0:
                check = False
                break # 나눠지는 수가 존재하면 소수가 아니므로 break
        if check:
            prime.append(i)

if len(prime) == 0:
    print("-1")
else:
    print(sum(prime))
    print(min(prime))