def solution(id_list, report, k):
    answer = []
    
    report_dic = {}
    reported_dic = {}
    
    for i in id_list:
        report_dic[i] = []
        reported_dic[i] = set()  # 각 유저가 신고한 아이디를 중복 없이 저장하기 위해 set을 사용
    
    # 누가 누구를 신고했는지 찾기
    for r in report:
        reporter, reported = r.split()
        if reported not in report_dic[reporter]:
            report_dic[reporter].append(reported) 
        
    # 신고당한 사람을 key 값으로 잡아서 길이 비교, values가 k개 이상이면 정지
    for r in report:
        reporter, reported = r.split()
        reported_dic[reported].add(reporter)
    
    # 정지당한 회원 찾기
    stop_list = []
    for user_id, reporters in reported_dic.items():
        if len(reporters) >= k:
            stop_list.append(user_id)
    
    for user_id, reported in report_dic.items():
        count = 0
        for i in reported:
            if i in stop_list:
                count += 1
        answer.append(count)
        
    return answer