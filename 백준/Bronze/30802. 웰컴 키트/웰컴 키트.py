n = int(input())
applicant = list(map(int, input().split()))
t, p = map(int, input().split())

tshirts = 0

for i in applicant:
    if i == 0:
        continue
    tshirts += (i + t - 1) // t

print(tshirts)
print(n // p, n - p * (n // p))