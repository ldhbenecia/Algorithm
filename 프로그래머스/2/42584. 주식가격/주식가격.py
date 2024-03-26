from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        time = 0
        current = queue.popleft()
        
        for i in queue:
            time += 1
            if current > i:
                break
        answer.append(time)
            
    return answer