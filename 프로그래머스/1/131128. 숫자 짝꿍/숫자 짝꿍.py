def solution(X, Y):
    answer = ''
    count_X = [0] * 10
    count_Y = [0] * 10
    common = []
    
    for i in X:
        count_X[int(i)] += 1
    for i in Y:
        count_Y[int(i)] += 1
    
    for i in range(10):
        if count_X[i] > 0 and count_Y[i] > 0:
            common.extend([i] * min(count_X[i], count_Y[i]))

    common.sort(reverse = True)
    if not common:
        return '-1'
    elif common[0] == 0:
        return '0'
    else:
        answer = ''.join(map(str, common))
            
    return answer
