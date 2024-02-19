def solution(board, h, w):
    n = len(board)
    count = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = dx[i] + w
        ny = dy[i] + h
        
        if 0 <= nx < n and 0 <= ny < n:
            if board[h][w] == board[ny][nx]:
                count += 1
        
    return count