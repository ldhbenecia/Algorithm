import heapq

n = int(input())

lectures = []
max_day = 0

for i in range(n):
    p, d = map(int, input().split())
    lectures.append((d, p))
    max_day = max(max_day, d)

lectures.sort(reverse=True)  # 마감일 내림차순

result = 0
hq = []
idx = 0  # 하루 기록용

for day in range(max_day, 0, -1):
    # n일 전까지 당일 할 수 있는 강연 모두 넣기
    while idx < n and lectures[idx][0] >= day:
        heapq.heappush(hq, -lectures[idx][1])  # 최대힙
        idx += 1
    if hq:
        result += -heapq.heappop(hq)

print(result)

# 해쉬테이블로 p와 d를 엮는다.
# d를 오름차순으로 정렬한다.
# for문을 n만큼 돌려서 현재 i값에 속한 key값 중에 가장 큰 값을 result에 더한다.

# 위의 방식으로 풀면 날짜별로 가장 비싼 강연만을 고르게 된다.
# 하지만 (50, 2), (20, 2), (10, 1), (5, 1)이 있다고 가정하면 위의 방식으로는
# 1일 때 10, 2일때 50을 골라서 60을 택한다.
# 하지만 이는 첫째날에 20, 둘째날에 50을 택하면 70으로 더 큰 해를 구할 수 있다.
# 그렇기 때문에 반례의 탄생으로 날짜별로 정렬해서 이익이 가장 큰 것을 고르는 것은 틀릴 수 있다.

# 마감일 기준으로 모든 날짜를 구해서 최적의 해를 구해야한다.
# 우선순위큐 (Heap)을 사용해보자.,
# 모든 강연을 마감일 기준으로 정렬한 뒤, 각 날짜에 할 수 있는 강연 중 가장 이익이 큰 것을 택해야한다.
# 위의 반례를 해결할 수 있어야한다.
# 첫 예시는 날짜에 따라서만 판별하나 우선순위 큐를 사용해서 각 날짜에 어떠한 제일 큰 값이 올 수 있는지를 모두 판별한다.
