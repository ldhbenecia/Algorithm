n = int(input())
meet = [tuple(map(int, input().split())) for _ in range(n)]

meet.sort(key=lambda x: (x[1], x[0]))

point = 0
result = 0
for start, end in meet:
    if point <= start:
        result += 1
        point = end
print(result)
