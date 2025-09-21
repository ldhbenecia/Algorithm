def hanoi(n, start, mid, end):
    # base
    if n == 1:
        print(start, end)
        return

    # start: 옮길 원판의 위치, end: 원판 도착 위치
    hanoi(n - 1, start, end, mid) # 가운데에 n-1개를 이동 시킴
    print(start, end)
    hanoi(n - 1, mid, start, end) # n-1개를 모두 마지막에 위치


k = int(input())
print(2**k - 1)
hanoi(k, 1, 2, 3)
