n = int(input())

if n == 0:
    print(0)
else:
    opinion = sorted([int(input()) for _ in range(n)])
    remove = round(n * 0.15 + 0.0000001)

    if remove > 0 : opinion = opinion[remove:-remove]
    sum_value = sum(opinion)
    print(round(sum_value / len(opinion) + 0.0000001))
