from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    answer = 0
    
    people = deque(people)
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit:
            answer += 1
            people.pop()
            people.popleft()
        else:
            answer += 1
            people.popleft()
            
    if people:
        answer += 1
        
    return answer

# 정렬 후 가장 무거운 사람과 가장 가벼운 사람을 합함
# 그 합한 값이 limit보다 작으면 함께 내리고 그렇지 않다면 무거운 사람만 내릴 것

