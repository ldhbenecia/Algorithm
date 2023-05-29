def solution(name, yearning, photo):
    answer = []
    info = dict(zip(name, yearning))
    
    for i in photo:
        sum = 0
        print(i)
        for j in i:
            sum += info.get(j, 0)
        answer.append(sum)
        
    return answer
