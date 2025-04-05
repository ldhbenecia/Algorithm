n, k = map(int, input().split())
lst = list(map(int, input().split()))

temp = sum(lst[:k])
result = temp

for i in range(n - k):
    temp = temp - lst[i] + lst[k + i]
    if temp > result:
        result = temp

print(result)
