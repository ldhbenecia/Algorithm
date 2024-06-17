def solution(topping):
    answer = 0
    
    chulsoo = {}
    for i in topping:
        if i in chulsoo:
            chulsoo[i] += 1
        else:
            chulsoo[i] = 1
    
    brother = {}
    for i in topping:
        if len(chulsoo) == len(brother):
            answer += 1
        
        if i not in brother:
            brother[i] = 1
        
        chulsoo[i] -= 1
        if chulsoo[i] == 0:
            del chulsoo[i]
        
    return answer