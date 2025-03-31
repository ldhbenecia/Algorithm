a, b, c = map(int, input().split())

distance = [0] * 101
for i in range(3):
    x, y = map(int, input().split())
    
    for j in range(x, y):
        distance[j] += 1

result = 0
for i in distance:
    if i == 1:
        result += a
    elif i == 2:
        result += b * 2
    elif i == 3:
        result += c * 3

print(result)