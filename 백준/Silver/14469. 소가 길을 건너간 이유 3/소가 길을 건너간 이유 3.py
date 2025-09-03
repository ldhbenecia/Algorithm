n = int(input())
cow = [tuple(map(int, input().split())) for _ in range(n)]

cow.sort()

result = -1
for i in range(n):
    if cow[i][0] >= result:
        result = cow[i][0] + cow[i][1]
    else:
        result += cow[i][1]

print(result)
