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
        else:
            end -= 1
            answer += 1
    
    # 마지막 한 사람이 남았다면
    if start == end:
        answer += 1
        
    return answer

# 정렬 후 가장 무거운 사람과 가장 가벼운 사람을 합함
# 그 합한 값이 limit보다 작으면 함께 내리고 그렇지 않다면 무거운 사람만 내릴 것

