T = int(input())

for _ in range(T):
    A, B, N = map(int, input().split())

    if A > N or B > N:
        print(1)
        continue
    
    x, y = A, B
    cnt = 0
    
    while x <= N and y <= N:
        if x < y:
            x += y
        else:
            y += x
        cnt += 1
        
    print(cnt)
    