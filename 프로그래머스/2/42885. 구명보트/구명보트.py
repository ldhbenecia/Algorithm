def solution(people, limit):
    people.sort()
    
    answer = 0
    start = 0
    end = len(people) - 1
    
    while start < end:
        if people[end] + people[start] <= limit:
            start += 1
            
        end -= 1
        answer += 1
    
    # 마지막 한 사람이 남았다면
    if start == end:
        answer += 1
        
    return answer