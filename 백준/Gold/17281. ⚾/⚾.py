from itertools import permutations
import sys

input = sys.stdin.readline

N = int(input())
war = [list(map(int, input().split())) for _ in range(N)]


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


players = [2, 3, 4, 5, 6, 7, 8, 9]  # 1번은 4번 타자 고정
result = 0

for perm in permutations(players):
    # 타순 구성
    order = [0] * 9
    order[3] = 1
    idx = 0

    for pos in range(9):  # 0~8까지 돌며 타순 채우기
        if pos == 3:  # 4번 타자 자리 건너 뛰기
            continue
        order[pos] = perm[idx]
        idx += 1

    result = max(result, simulate(order))
print(result)
