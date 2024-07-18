def solution(skill, skill_trees):
    answer = 0
    
    temp_lst = []
    for i in skill_trees:
        temp = ""
        for j in i:
            if j in skill:
                temp += j
            else:
                continue
        temp_lst.append(temp)
        
    for j in temp_lst:
        if skill[:len(j)] == j:
            answer += 1
        else:
            continue
    
    return answer
