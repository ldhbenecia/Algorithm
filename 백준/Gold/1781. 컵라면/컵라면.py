import heapq

n = int(input())

problem = []

for i in range(n):
    d, c = map(int, input().split())
    problem.append((d, c))

problem.sort()

hq = []
for d, c in problem:
    heapq.heappush(hq, c)
    if len(hq) > d:
        heapq.heappop(hq)

print(sum(hq))
