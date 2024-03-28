import heapq

def solution(jobs):
    answer, work, now = 0, 0, 0
    start = -1
    heap = []

    while work < len(jobs):
        for i in jobs:
            if start < i[0] <= now:
                heapq.heappush(heap, [i[1], i[0]])
                
        if heap:
            current_work = heapq.heappop(heap)
            start = now
            now += current_work[0]
            answer += now - current_work[1]
            work += 1
        else:
            now += 1

    return answer // len(jobs)
