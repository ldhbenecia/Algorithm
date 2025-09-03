import heapq

n = int(input())

lectures = []

for i in range(n):
    p, d = map(int, input().split())
    lectures.append((p, d))

lectures.sort(key=lambda x: x[1])

hq = []
for p, d in lectures:
    heapq.heappush(hq, p)
    if len(hq) > d:
        heapq.heappop(hq)

print(sum(hq))
