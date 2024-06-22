def solution(s):
    answer = []
    
    s = s[2:-2].split('},{')
    s = [i.split(',') for i in s]
    
    s.sort(key=len)
    
    for i in s:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
            
    return answer