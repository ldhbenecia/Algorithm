import heapq

n, k = map(int, input().split())
jewal = [tuple(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

jewal.sort(key=lambda x: x[0])
bags.sort()

hq = []
result = 0
idx = 0

# 가방마다 담을 수 있는 보석 중에 가장 비싼 것을 골라야하기 때문에 최대힙 사용
for bag_weight in bags:
    while idx < n and jewal[idx][0] <= bag_weight:
        heapq.heappush(hq, -jewal[idx][1])
        idx += 1
    if hq:
        result += -heapq.heappop(hq)

print(result)
