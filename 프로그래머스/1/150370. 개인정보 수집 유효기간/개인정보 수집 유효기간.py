def solution(today, terms, privacies):
    answer = []
    term_dict = {}
    
    for i in terms:
        kind, period = i.split()
        term_dict[kind] = int(period)
    
    for idx, i in enumerate(privacies):
        day, kind = i.split()
        yy, mm, dd = map(int, day.split('.'))
        
        term_years = term_dict[kind] // 12
        term_months = term_dict[kind] % 12
        
        ## 년도에 대한 처리
        yy += term_years
        
        # 달에 대한 처리
        mm += term_months
        if mm > 12:
            yy += 1                                           
            mm -= 12
        
        # 일에 대한 처리
        dd -= 1
        if dd == 0:
            mm -= 1
            if mm == 0:
                yy -= 1
                mm = 12
            dd = 28
        
        today_yy, today_mm, today_dd = map(int, today.split('.'))
        yy, mm, dd = int(yy), int(mm), int(dd)
        if yy < today_yy:
            answer.append(idx + 1)
        if yy == today_yy and mm < today_mm:
            answer.append(idx + 1)
        if yy == today_yy and mm == today_mm and dd < today_dd:
            answer.append(idx + 1)
    
    return answer
