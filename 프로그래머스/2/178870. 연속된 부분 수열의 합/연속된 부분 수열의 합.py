def solution(sequence, k):
    answer = []
    left, right = 0, 0
    sequence_sum = sequence[0]
    
    if sequence_sum == k:
        return [0, 0]
    
    while True:
        if sequence_sum <= k:
            right += 1
            if right == len(sequence):
                break
            sequence_sum += sequence[right]
        else:
            left += 1
            sequence_sum -= sequence[left - 1]
        
        if sequence_sum == k:
            answer.append([left, right])
    
    answer.sort(key = lambda x : (x[1] - x[0], x[0]))
    return answer[0]