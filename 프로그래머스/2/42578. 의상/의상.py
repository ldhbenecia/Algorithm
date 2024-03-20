def solution(clothes):
    answer = 1
    dic = {}
    
    for name, kind in clothes:
        if kind in dic.keys():
            dic[kind] += [name]
        else:
            dic[kind] = [name]
    
    for kind, name in dic.items():
        answer *= len(name) + 1
        
    return answer - 1

