def solution(m, n, board):
    answer = 0
    board = list(map(list, board))

    while True:
        filter = [[0 for _ in range(n)] for _ in range(m)]
        has_removal = False
        
        for i in range(m - 1):
            for j in range(n - 1):
                a = board[i][j] # 현재 값
                b = board[i][j+1] # 그 오른쪽 값
                c = board[i+1][j] # 그 아래 값
                d = board[i+1][j+1] # 그 오른쪽 아래 대각 값
                if a == b == c == d and a != '0':
                    filter[i][j], filter[i][j+1], filter[i+1][j], filter[i+1][j+1] = 1, 1, 1, 1
                    has_removal = True
                    
        if has_removal:
            for i in range(m):
                for j in range(n):
                    if filter[i][j] == 1:
                        board[i][j] = '0'
                        answer += 1
        else:
            break
        
        # 2차원 리스트를 세로로 읽기 & 아래서부터 읽기
        for j in range(n):
            empty_spaces = []
            for i in range(m - 1, -1, -1):
                if board[i][j] == '0':
                    empty_spaces.append(i)
                elif empty_spaces:
                    empty_idx = empty_spaces.pop(0)
                    board[empty_idx][j] = board[i][j]
                    board[i][j] = '0'
                    empty_spaces.append(i)
                       
    return answer