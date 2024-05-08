def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    limit_case = ['-', '_', '.']
    for i in new_id:
        if i.isalpha() or i.isnumeric() or i in limit_case:
            answer += i

    # 3단계 (2번 이상이므로 if가 아닌 전 값과 중복해서 비교해야하기 때문에 while)
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    # 4단계
    if len(answer) > 0:
        if answer[0] == '.':
            answer = answer[1:]
    
    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[:-1]

    # 5단계
    if not answer:
        answer = 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    if len(answer) <= 2:
        while True:
            if len(answer) == 3:
                break
            else:
                last = answer[-1]
                answer += last

    return answer