def solution(sizes):
    answer = 0
    width = []
    height = []
    
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            width.append(sizes[i][0])
            height.append(sizes[i][1])
        else:
            width.append(sizes[i][1])
            height.append(sizes[i][0])
    
    answer = max(width) * max(height)
    
    return answer