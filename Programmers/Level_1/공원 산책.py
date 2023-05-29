def solution(park, routes):    
    # park = 지도, routes = 이동 루트
    # 시작 지점 찾기
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == "S": # 시작 지점 세팅
                start_row = i
                start_col = j
    
    # 이동 방향 정의
    op = {"N":(-1,0), "S":(1,0), "W":(0,-1), "E":(0,1)}
    
    for i in routes:
        d, n = i.split() # 방향, 몇칸 이동할지 횟수
        n = int(n)
        dx, dy = start_row, start_col # 시작 좌표 저장
        
        for _ in range(n):
            nx = start_row + op[d][0] # 이동할 위치 -> 현재 행 + 이동 행
            ny = start_col + op[d][1] # 이동할 위치 -> 현재 열 + 이동 열
            
            # 주어진 방향으로 이동 중 내부에 있고 장애물 아니면 이동
            if 0 <= nx <= len(park)-1 and 0 <= ny <= len(park[0])-1 and park[nx][ny] != "X":
                start_row, start_col = nx, ny # 이동
            else: # 외부로 가거나 장애물 만났을 때
                start_row, start_col = dx, dy # 그대로
                break # 다음 동작 실행하기 위해 이 for문에서 탈출
    
    return (start_row, start_col)