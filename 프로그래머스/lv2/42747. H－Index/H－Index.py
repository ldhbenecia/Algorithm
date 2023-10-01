def solution(citations):
    answer = 0
    citations.sort()
    for h in range(len(citations) + 1):
        count = 0
        for i in citations:
            if i >= h:
                count += 1
        if count >= h:
            answer = h
    return answer

    # 0 1 3 5 6
    # 조건 1: n편 중 h번 이상 인용된 논문
    # 조건 2: 나머지 논문은 h번 이하
    
    # h가 0이면
    # 1. 5편 중 0번 이상 인용된 논문 0편 이상 0 1 3 5 6
    # 2. 나머지 논문 5개 0번 이하 인용 5 >= 0 가능
    
    # h가 1이면
    # 1. 5편 중 1번 이상 인용된 논문 1편 이상 1 3 5 6
    # 2. 나머지 논문 4개 1번 이하 인용 4>=1 가능
    
    # h가 2
    # 1. 5편 중 2번 이상 인용된 논문 2편 이상 3 5 6
    # 2. 나머지 논문 3개 2번 이하 인용 3>=2 가능
    
    # h가 3
    # 1. 5편 중 3번 이상 인용된 논문 3편 이상 3 5 6
    # 2. 나머지 논문 2개 3번 이하 인용 3 >= 3 가능 
    
    # h가 4는 이제 5, 6인데 4번 이하 인용 2 >= 4 불가능
    