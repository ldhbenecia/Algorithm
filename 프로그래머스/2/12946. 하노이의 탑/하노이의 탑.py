def hanoi(n, start, end, mid):
    answer = []
    
    if n == 1:
        answer.append((start, end))
    else:
        # 시작 기둥에서 보조 기둥으로 대상 기둥을 활용해서
        answer.extend(hanoi(n - 1, start, mid, end))
        # 시작 기둥에서 대상 기둥으로
        answer.append((start, end))
        # 보조 기둥에서 대상 기둥으로 시작기둥을 활용해서
        answer.extend(hanoi(n - 1, mid, end, start))
        
    return answer

def solution(n):
    return hanoi(n, 1, 3, 2)
