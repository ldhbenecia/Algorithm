n = int(input())
player = [input() for _ in range(n)]

result = []

for i in range(n):
    cnt = 0
    current = player[i][0]
    for j in range(n):
        if player[j][0] == current:
            cnt += 1

    if cnt >= 5:
        result.append(current)

if not result:
    print("PREDAJA")
    exit()

result_lst = []
for i in result:
    if i not in result_lst:
        result_lst.append(i)

result_lst.sort()

for i in result_lst:
    print(i, end="")
