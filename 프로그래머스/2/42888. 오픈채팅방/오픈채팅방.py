def solution(record):
    answer = []
    dic = {}
    
    # 닉네임 변환 작업
    for i in record:
        i = i.split()
        if i[0] == "Enter":
            dic[i[1]] = i[2]
        if i[0] == "Change":
            dic[i[1]] = i[2]
    
    # 변환한 닉네임 적용
    for i in record:
        i = i.split()
        if i[0] == "Enter":
            answer.append(f'{dic[i[1]]}님이 들어왔습니다.')
            
        if i[0] == "Leave":
            answer.append(f'{dic[i[1]]}님이 나갔습니다.')
            
    return answer