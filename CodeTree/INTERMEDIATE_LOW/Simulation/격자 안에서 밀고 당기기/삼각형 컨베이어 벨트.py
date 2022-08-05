n, t = tuple(map(int, input().split()))
l = list(map(int, input().split()))
r = list(map(int, input().split()))
b = list(map(int, input().split()))

for _ in range(t):
    
    # temp 저장
    temp1 = l[n - 1]
    temp2 = r[n - 1]

    for i in range(n - 1, 0, -1):
        l[i] = l[i - 1]
    l[0] = b[n - 1]

    for i in range(n - 1, 0 , -1):
        r[i] = r[i - 1]
    r[0] = temp1

    for i in range(n - 1, 0, -1):
        b[i] = b[i - 1]
    b[0] = temp2

for i in l:
    print(i, end = ' ')

print()

for i in r:
    print(i, end = ' ')

print()

for i in b:
    print(i, end = ' ')