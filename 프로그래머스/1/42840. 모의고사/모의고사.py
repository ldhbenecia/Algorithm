def solution(answers):
    answer = []
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1, c2, c3 = 0, 0, 0
    
    for i in range(len(answers)):
        if answers[i] == a1[i % 5]:
            c1 += 1
        if answers[i] == a2[i % 8]:
            c2 += 1
        if answers[i] == a3[i % 10]:
            c3 += 1
            
    high = max(c1, c2, c3)
    
    if high == c1:
        answer.append(1)
    if high == c2:
        answer.append(2)
    if high == c3:
        answer.append(3)

    return answer