t = int(input())

for _ in range(t):
    n = int(input())
    count = 0
    temp = 5
    
    while temp <= n:
        count += n // temp
        temp *= 5
        
    print(count)