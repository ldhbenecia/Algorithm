from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())

    dic = defaultdict(int)
    for _ in range(n):
        clothe = input().split()
        name, kind = clothe[0], clothe[1]
        dic[kind] += 1

    result = 1
    for i in dic.values():
        result *= i + 1
    
    result -= 1
    print(result)
