t = int(input())

for _ in range(t):
    n = int(input())
    dic = {}

    for _ in range(n):
        name, kind = input().split()
        if kind not in dic:
            dic[kind] = 1
        else:
            dic[kind] += 1

    result = 1
    for kind in dic:
        result *= dic[kind] + 1 # headgear가 2개이면, 돌아가면서 입는 경우의 수 2 + 아예 안 입는 경우의 수 1

    print(result - 1) # 나체 제외
