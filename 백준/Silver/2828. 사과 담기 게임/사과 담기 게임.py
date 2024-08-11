n, m = map(int, input().split())
j = int(input())
position = [int(input()) for _ in range(j)]

start = 1
end = m
count = 0

for i in position:
    if i > end:
        count += (i - end)
        start += (i - end)
        end = i
    elif i < start:
        count += (start - i)
        end -= (start - i)
        start = i

print(count)
