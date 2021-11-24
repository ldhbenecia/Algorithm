n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
    
answer = 0
a.sort()

for i in range(n):
    answer += a[i] * b.pop(b.index(max(b)))
    
print(answer)