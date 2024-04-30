def solution(k, m, score):
    answer = 0
    score.sort(reverse = True)
    stack = []
    
    for i in score:
        if len(stack) < m:
            stack.append(i)
            if len(stack) == m:
                answer += min(stack) * m
                stack.clear()
        
    return answer