def solution(N, stages):
    dic = {}
    answer = []
    challenger_cnt = len(stages)
    fail_count_list = [0]
    
    for i in range(1, N + 1):
        fail_count_list.append(stages.count(i))
    
    for i in range(1, N + 1):
        if challenger_cnt != 0:
            dic[i] = (fail_count_list[i] / (challenger_cnt))
            challenger_cnt -= fail_count_list[i]
        else:
            dic[i] = 0
            
    answer = sorted(dic, key=lambda x : dic[x], reverse=True)
    
    return answer