import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        most_low, low = heapq.heappop(scoville), heapq.heappop(scoville)
        formula = most_low + (low * 2)
        heapq.heappush(scoville, formula)
        answer += 1
    
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
    return answer