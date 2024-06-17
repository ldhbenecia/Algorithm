def solution(want, number, discount):
    answer = 0
    
    dic = {}
    
    for i in want:
        dic[i] = 0
    
    for i in range(len(number)):
        dic[want[i]] = number[i]
    
    first_day = 0
    #end_day = first_day + 9
    for day, kind in enumerate(discount):
        end_day = day + 9
        
        day_dic = {}
        for i in discount[day:end_day + 1]:
            if i not in dic:
                break
            
            if i not in day_dic:
                day_dic[i] = 1
            else:
                day_dic[i] += 1
        
        all_match = True
        for item in dic:
            if day_dic.get(item) != dic[item]:
                all_match = False
                break
        
        if all_match:
            answer += 1
            
    return answer