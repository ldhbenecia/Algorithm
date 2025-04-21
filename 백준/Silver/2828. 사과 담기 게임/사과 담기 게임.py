n, m = map(int, input().split())
j = int(input())
position = [int(input()) for _ in range(j)]
position = list(
    map(lambda x: x - 1, position)
)  # position은 인덱스형 위치값이 아니므로 -1씩 해서 처리

move = 0
left = 0
right = m - 1

for i in position:
    # 1. 가만히 있어도 바구니에 사과가 떨어지는 경우
    if left <= i <= right:
        continue

    # 2. 사과가 떨어지는 위치가 왼쪽에 있는 경우
    elif i < left:
        distance = left - i  # 가야할 거리
        move += distance
        left -= distance
        right -= distance

    # 3. 사과가 떨어지는 위치가 오른쪽인 경우
    else:  # i > right:
        distance = i - right  # 가야할 거리
        move += distance
        left += distance
        right += distance


print(move)
