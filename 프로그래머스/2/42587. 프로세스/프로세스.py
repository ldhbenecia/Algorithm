def solution(priorities, location):
    answer = 0
    queue = [(p, idx) for idx, p in enumerate(priorities)]

    while queue:
        current_priority, current_idx = queue.pop(0)
        if any (current_priority < p for p, idx in queue):
            queue.append((current_priority, current_idx))
        else:
            answer += 1
            if location == current_idx:
                break
        
    return answer

