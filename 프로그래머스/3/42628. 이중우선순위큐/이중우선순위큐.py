import heapq

def solution(operations):
    answer = []
    
    for operate in operations:
        command, value = operate.split()
        value = int(value)
        
        if command == "I":
            heapq.heappush(answer, value)
        if command == "D":
            if answer and value == 1:
                answer.pop()
            if answer and value == -1:
                heapq.heappop(answer)
    
    if not answer:
        answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]
        
    return answer