def solution(wallpaper):
    answer = []
    
    lux, luy = 0, 0
    rdx, rdy = 0, 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                answer.append((i, j))
    
    lux = min(answer)[0]
    luy = min(answer, key=lambda x: x[1])[1]
    rdx = max(answer)[0] + 1
    rdy = max(answer, key=lambda x: x[1])[1] + 1
    
    
    return [lux, luy, rdx, rdy]