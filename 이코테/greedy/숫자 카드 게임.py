n, m = map(int,input().split())

result = 0

for i in range(n):
    num = list(map(int,input().split()))
    min_num = min(num)
    result = max(result, min_num)
    
print(result)