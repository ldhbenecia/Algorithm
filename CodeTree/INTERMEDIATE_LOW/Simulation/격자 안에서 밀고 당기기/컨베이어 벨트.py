n, t = tuple(map(int, input().split()))
u = list(map(int, input().split()))
d = list(map(int, input().split()))

for _ in range(t):
    # 위에서 가장 오른쪽 값 따로 저장
    temp = u[n - 1]

    # 위에 줄 (u) 완성
    for i in range(n - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = d[n - 1] # 위에의 맨 왼쪽 값은 아래의 제일 오른쪽 값이 옴

    # 아래 줄 (d) 완성
    for i in range(n - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = temp

for i in u:
    print(i, end = ' ')

print()

for i in d:
    print(i, end = ' ')