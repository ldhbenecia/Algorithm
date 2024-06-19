def hanoi(n, start, mid, end):
    answer = []
    
    if n == 1:
        answer.append((start, end))
    else:
        # Step 1: n-1 개의 원판을 start에서 end를 거쳐 mid로 옮기기
        answer.extend(hanoi(n - 1, start, end, mid))
        # Step 2: 남은 1개의 원판을 start에서 end로 옮기기
        answer.append((start, end))
        # Step 3: n-1 개의 원판을 mid에서 start를 거쳐 end로 옮기기
        answer.extend(hanoi(n - 1, mid, start, end))
    
    return answer

def solution(n):
    return hanoi(n, 1, 2, 3)
