def solution(data, ext, val_ext, sort_by):
    answer = []
    dict = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    
    for i in data:
        if i[dict[ext]] < val_ext:
            answer.append(i)
            
    answer.sort(key = lambda x : x[dict[sort_by]])
    
    return answer