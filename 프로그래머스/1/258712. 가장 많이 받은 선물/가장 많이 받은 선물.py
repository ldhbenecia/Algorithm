def solution(friends, gifts):
    dic = {}
    gifts_between = {}
    
    for i in friends:
        dic[i] = [0, 0, 0] # 준 선물, 받은 선물, 선물 지수
        gifts_between[i] = {}
    
    for i in gifts:
        A, B = i.split() # 선물 준 사람, 받은 사람
        
        dic[A][0] += 1 # 준 선물
        dic[B][1] += 1 # 받은 선물
    
        # 선물 지수
        dic[A][2] = dic[A][0] - dic[A][1]
        dic[B][2] = dic[B][0] - dic[B][1]
        
        # 누가 누구에게 몇 개의 선물을 주었는지 체크
        if B in gifts_between[A]:
            gifts_between[A][B] += 1
        else:
            gifts_between[A][B] = 1

    
    gifts_num = [0 for _ in friends]
    for i in range(len(friends)):
        curr = friends[i]
        for j in range(i + 1, len(friends)):
            another = friends[j]
            
            if another in gifts_between[curr]:
                a = gifts_between[curr][another] # curr -> another
            else:
                a = 0
            
            if curr in gifts_between[another]:
                b = gifts_between[another][curr] # another -> curr
            else:
                b = 0
    
            if a > b:
                gifts_num[i] += 1
            elif a < b:
                gifts_num[j] += 1
            elif a == b:
                ai, bi = dic[curr][2], dic[another][2] # 선물 지수
                if ai > bi:
                    gifts_num[i] += 1
                elif ai < bi:
                    gifts_num[j] += 1

    return max(gifts_num)