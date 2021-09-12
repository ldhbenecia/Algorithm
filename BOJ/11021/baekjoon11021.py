t = int(input())
sum = 0

for i in range(t):
    a, b = map(int, input().split())
    sum = a + b
    print(f"Case #{i+1}: {sum}")