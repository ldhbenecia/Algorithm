T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    X = list(map(int, input().split()))

    # 원래 맨해튼 합 S = sum |X[i] - X[i-1]|
    S = 0
    for i in range(1, N):
        S += abs(X[i] - X[i - 1])

    result = 1e9

    # k = 건너뛸 체크포인트
    for k in range(1, N - 1):
        # 현재 k는 건너뛰어야 함
        # 현재 K를 기준으로 구해지는 맨해튼거리 한칸 앞 뒤 체크포인트의 거리는 빼기
        # 예시에서 X4가 방문하지 않을때 x5-x3을 했던것처럼 앞뒤의 값을 가지고 더하기
        delta = -abs(X[k] - X[k - 1]) - abs(X[k + 1] - X[k]) + abs(X[k + 1] - X[k - 1])
        result = min(result, S + delta)

    print(result)
