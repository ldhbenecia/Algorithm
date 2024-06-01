n = int(input())
position = sorted(list(map(int, input().split())))

mid = (n - 1) // 2
print(position[mid])