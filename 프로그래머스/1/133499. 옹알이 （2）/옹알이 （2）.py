def solution(babbling):
    possible = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    
    for i in babbling:
        for word in possible:
            if word * 2 not in i: # 연속해서 같은 발음
                i = i.replace(word, ' ')
        if len(i.strip()) == 0:
            answer += 1
        
    return answer