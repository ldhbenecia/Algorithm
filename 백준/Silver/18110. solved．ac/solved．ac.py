import math

def custom_round(num):
    if num - int(num) >= 0.5:
        return math.ceil(num)
    else:
        return math.floor(num)

n = int(input())

if n == 0:
    print(0)
else:
    opinion = sorted([int(input()) for _ in range(n)])
    remove = custom_round(n * 0.15)

    if remove > 0 : opinion = opinion[remove:-remove]
    sum_value = sum(opinion)
    print(custom_round(sum_value / len(opinion)))
