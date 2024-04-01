def solution(citations):
    answer = 0
    citations.sort()
    for h in range(len(citations) + 1):
        count = 0
        for i in citations:
            if i >= h:
                count += 1
        if count >= h:
            answer = h
    return answer
