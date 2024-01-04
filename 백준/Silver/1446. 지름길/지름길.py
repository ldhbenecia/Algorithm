n, d = map(int, input().split())
road = [list(map(int, input().split())) for _ in range(n)]
distance = [i for i in range(d + 1)]

for i in range(d + 1):
  distance[i] = min(distance[i], distance[i - 1] + 1)
  for start, end, short in road:
    if i == start and end <= d and distance[i] + short < distance[end]:
      distance[end] = distance[i] + short
      
print(distance[-1])