def solution(k, score):
    honor = []
    answer = []
    
    n = 1;
    for i in score:
        if k >= n:
            honor.append(i)
            honor.sort(reverse=True)
            answer.append(honor[-1])
            n += 1
        else:
            if i > honor[-1]:
                honor.pop()
                honor.append(i)
                honor.sort(reverse=True)
                answer.append(honor[-1])
            else:
                answer.append(honor[-1])
    
    return answer
