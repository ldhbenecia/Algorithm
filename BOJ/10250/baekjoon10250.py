t = int(input())

for i in range(t):
    h, w, n = map(int,input().split())
    floor = n % h
    unit = n // h + 1

    if n % h == 0:
        floor = h
        unit = n // h
    print(f"{floor*100+unit}")