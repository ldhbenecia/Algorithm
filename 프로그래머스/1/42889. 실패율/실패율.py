def solution(N, stages):
    dic = {}
    answer = []
    challenger_cnt = len(stages)
    
    for i in range(1, N + 1):
        if challenger_cnt != 0:
            dic[i] = (stages.count(i) / (challenger_cnt))
            challenger_cnt -= stages.count(i)
        else:
            dic[i] = 0
            
    answer = sorted(dic, key=lambda x : dic[x], reverse=True)
    
    return answer