n = int(input())
x, y = 0, 0 #현재위치

# E, W, S, N
# 동, 서, 남, 북 순으로의 이동 값
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

for _ in range(n):
    a, b = input().split() # a = 방향, b = 움직인 거리
    b = int(b)

    # 입력된 문자를 인덱스 순서로 치환해서 호출하게끔 구성
    if a == 'E': #동
        move = 0
    elif a == 'W': #서
        move = 1
    elif a == 'S': #남
        move = 2
    else: #북
        move = 3
    x += dx[move] * b
    y += dy[move] * b

print(x, y)