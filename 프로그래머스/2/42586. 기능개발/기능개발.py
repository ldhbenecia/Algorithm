def solution(progresses, speeds):
    answer = []
    period = []
    
    for progress, speed in zip(progresses, speeds):
        item = 100 - progress
        if item % speed == 0:
            period.append(item // speed)
        else:
            period.append(item // speed + 1)
    
    idx = 0
    for i in range(len(period)):
        if period[idx] < period[i]:
            print(period[idx], period[i])
            answer.append(i - idx)
            idx = i
    
    answer.append(len(period) - idx)
    
    return answer
