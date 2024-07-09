def solution(elements):
    unique_sum = set()
    circle = extended_elements = elements * 2
    
    for i in range(1, len(elements) + 1):
        for j in range(len(elements)):
            current = sum(circle[j: j + i])
            unique_sum.add(current)
    
    return len(unique_sum)