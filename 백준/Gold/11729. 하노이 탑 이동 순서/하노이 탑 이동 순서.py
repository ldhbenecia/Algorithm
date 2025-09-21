def hanoi(n, start, end, temp):
    global cnt, path
    # base
    if n == 1:
        cnt += 1
        path.append((start, end))
        return

    # start: 옮길 원판의 위치, end: 원판 도착 위치
    hanoi(n - 1, start, temp, end)
    cnt += 1
    path.append((start, end))
    hanoi(n - 1, temp, end, start)  # n-1개를 모두 마지막에 위치,


# 원판이 3개라고 가정할 시 제일 아래에 있는 원판을 end 지점으로 옮기기 위해 그 위의 n-1개의 원판을 mid에 옮긴다.
# 시작점: start, 도착지점: temp, temp: end
# 그 후 temp에 있는 원판을 end로 옮긴다. 시작점: temp, 도착지점: end, temp: start
# 가장 마지막 원판은 출력하면 끝

k = int(input())

cnt = 0
path = []

hanoi(k, 1, 3, 2)
print(cnt)
for i, j in path:
    print(i, j)
