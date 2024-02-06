n = int(input())
m = int(input())
x = list(map(int, input().split()))

result = []
max_distance = max(x[0], n - x[-1])
result.append(max_distance)

for i in range(1, m):
  distance = (x[i] - x[i - 1] + 1) // 2
  result.append(distance)

print(max(result))
