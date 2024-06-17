def solution(want, number, discount):
    answer = 0
    
    # want, number 딕셔너리 초기화
    dic = {}
    for i in range(len(number)):
        dic[want[i]] = number[i]
    
    for day, kind in enumerate(discount):
        end_day = day + 9
        
        # 10일간의 할인상품 목록 딕셔너리 초기화
        day_dic = {}
        for i in discount[day:end_day + 1]:
            # want에 없는 항목이면 바로 배제
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