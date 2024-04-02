def solution(sizes):
    width = []
    height = []
    
    for i in sizes:
        if i[0] > i[1]:
            width.append(i[0])
            height.append(i[1])
        else:
            width.append(i[1])
            height.append(i[0])
            
    return max(width) * max(height)