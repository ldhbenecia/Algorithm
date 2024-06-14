def solution(storey):
    answer = 0
    
    while storey:
        first = storey % 10
        
        if first < 5:
            answer += first
        elif first > 5:
            answer += 10 - first
            storey += 10
        else:
            if storey // 10 % 10 < 5:
                answer += first
            else:
                answer += 10 - first
                storey += 10

        storey //= 10

    return answer
