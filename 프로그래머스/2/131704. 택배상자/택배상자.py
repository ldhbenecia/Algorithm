def solution(order):
    answer = 0
    
    belt = [] # 보조 컨테이너 벨트
    idx = 0
    
    for i in range(1, len(order) + 1):
        belt.append(i)
        
        while belt and belt[-1] == order[idx]:
            answer += 1
            idx += 1
            belt.pop()
    
    return answer
