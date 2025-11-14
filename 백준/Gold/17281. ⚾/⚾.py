import sys

input = sys.stdin.readline

N = int(input())
war = [list(map(int, input().split())) for _ in range(N)]

order = [0] * 9  # 선수 배치할 타순 테이블
order[3] = 1  # 4번 타자는 1번 선수 고정

# 방문 체크: 선수번호 기준(1~9)
visited = [False] * 10
visited[1] = True # 1번 선수는 이미 정해져있음

result = 0
def simulate(order):
    # 타순으로 N이닝 시뮬레이션
    score = 0
    batter_idx = 0  # 현재 타석 (타순 인덱스)

    for inning in range(N):
        outCount = 0
        b1 = b2 = b3 = 0  # 진루 상황 (없는걸로 초기화)

        while outCount < 3:
            plyaer = order[batter_idx]
            result = war[inning][plyaer - 1]

            if result == 0:
                outCount += 1
            elif result == 1:  # 안타
                score += b3  # 안타를 쳤을 때 b3에 선수가 있다면 득점 score++
                b3, b2, b1 = b2, b1, 1  # 한칸씩 진루
            elif result == 2:
                score += b2 + b3
                b3, b2, b1 = b1, 1, 0
            elif result == 3:
                score += b1 + b2 + b3
                b3, b2, b1 = 1, 0, 0
            else:  # 4 == 홈런
                score += 1 + b1 + b2 + b3
                b1 = b2 = b3 = 0

            batter_idx = (batter_idx + 1) % 9  # 댜음 타자 순환

    return score


def dfs(pos):
    # 타순을 백트래킹으로 채움
    # pos: 현재 채울 타순 인덱스(0 ~ 8) - 몇번 타석인지
    # 인덱스 3은 고정이라 건너뛰고 나머지에 2 ~ 9 배치
    global result

    # 고정 자리
    if pos == 3:
        dfs(4)
        return

    # 모든 자리를 채웠으면 시뮬
    if pos == 9:
        result = max(result, simulate(order))
        return

    # 1번 선수은 4번 타자이다.
    # 2번 선수부터 배치한다.
    # 2번 선수의 타순에 배치 되었는지 체크하고 안되어있으면 배치한다.
    # 현재 타순(pos), 0이라면 0은 여기서 1번 타석을 의미한다. (인덱스)
    # 1번 타석에 2번 타자를 배치하고 dfs 재귀를 굴린다.
    # 재귀가 돌면 pos(0+1)을 해서 2번 타석에 놓을 선수를 찾는다.
    # 재귀가 돌면서 다시 이 포문으로 왔을 때 range(2, 10)에서 2번 선수는
    # 이미 visited[2]는 True이기 때문에 건너띄고 3번 선수를 배치하게 된다.
    # 이렇게 모든 선수 배치를 하게 되어 pos == 9가 되면 이 타순 테이블로 시뮬레이션을 수행한다.
    # 시뮬레이션에서 나온 score 값을 받아서 return을 쳐서 재귀를 모두 푼다.
    # 풀면서 visited[plyaer]이랑 모두 False 처리한다.
    
    # dfs(0)으로 복귀가 되었으면 for문의 다음 후보를  진행한다.
    for plyaer in range(2, 10):  # 2 ~ 9번 선수 배치
        if not visited[plyaer]:
            visited[plyaer] = True
            order[pos] = plyaer
            dfs(pos + 1)
            visited[plyaer] = False
            order[pos] = 0


# 시작
dfs(0)
print(result)
