def solution(n):
    answer = []
    triangle = [[0 for j in range(1, i + 1)] for i in range(1, n + 1)]
    x, y = -1, 0 # 아래로 이동 초기값
    num = 1
    
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0: # 아래
                x += 1
            elif i % 3 == 1: # 오른쪽
                y += 1
            else: # 위
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1
            
    for i in range(n):
        for j in range(i + 1):
            answer.append(triangle[i][j])
        
    return answer
