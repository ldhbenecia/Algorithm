def solution(n, results):
    answer = 0
    
    ranks = [[0] * n for _ in range(n)]
    
    for a, b in results:
        ranks[a-1][b-1] = 1
        ranks[b-1][a-1] = -1
    
    # 플루이드 와셜
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j: continue
                
                # i가 k를 이기고 k가 j를 이기면 i가 j를 이김
                if ranks[i][k] == 1 and ranks[k][j] == 1:
                    ranks[i][j] = 1
                    ranks[j][i] = -1
                elif ranks[i][k] == -1 and ranks[k][j] == -1:
                    ranks[i][j] = -1
                    ranks[j][i] = 1
    
    # [[0, 1, 0, 0, 1], [-1, 0, -1, -1, 1], [0, 1, 0, -1, 1], [0, 1, 1, 0, 1], [-1, -1, -1, -1, 0]]
    # 1번 선수는 2, 5번 선수에게 승리
    # 2번 선수는 1, 3, 4번 선수한테 패배, 5번 선수에게 승리
    # 3번 선수는 2번, 5번 선수한테 승리, 4번 선수에게 패배
    # 4번 선수는 2, 3, 5번 선수한테 승리
    # 5번 선수는 1, 2, 3, 4번한테 패배
    
    # 0은 승부를 모르는 상태인데 본인과의 경기는 할 수 없음
    # 0이 1개인 경우, 다른 모두와 경기를 해봤기 때문에 정확하게 순위를 매길 수 있음
    for i in range(n):
        if ranks[i].count(0) == 1:
            answer += 1

    return answer