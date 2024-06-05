import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

for a in range(1, n + 1):
  for b in range(1, n + 1):
    if a == b:
      graph[a][b] = 0

for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_value = INF
person = 0
for i in range(1, n + 1):
  answer = sum(graph[i][1:]) # 1부터 n까지의 합
  if answer < min_value:
    min_value = answer
    person = i
    
# 여러 명일 경우 가장 작은 사람을 출력하라고 했으니 처음 정해진 min_value에 해당하는 사람
print(person)