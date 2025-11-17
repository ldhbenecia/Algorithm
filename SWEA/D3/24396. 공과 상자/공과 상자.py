T = int(input())

for _ in range(T):
    B, W, X, Y, Z = map(int, input().split())

    # Case 1: 검은 공은 검은 상자, 흰 공은 흰 상자
    black_in_black = B
    white_in_white = W
    black_in_white = 0
    white_in_black = 0
    score1 = (
        black_in_black * X
        + black_in_white * Z
        + white_in_white * Y
        + white_in_black * Z
    )

    # Case 2: 검은 공과 흰 공을 반대로 넣음 (가능한 만큼)
    black_in_white = min(B, W)
    black_in_black = B - black_in_white
    white_in_black = min(W, B)
    white_in_white = W - white_in_black
    score2 = (
        black_in_black * X
        + black_in_white * Z
        + white_in_white * Y
        + white_in_black * Z
    )

    # 최댓값
    print(max(score1, score2))
