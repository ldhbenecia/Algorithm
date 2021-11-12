n = list(map(int, input().split()))
sum = 0

for i in n:
    sum += i * i
    
print(sum%10)