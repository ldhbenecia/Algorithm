def solution(n):
    ans = 0
    
    # n에서 0으로
    while n != 0:
        # n이 짝수면 순간이동으로 도착 가능 (3에서 6으로 순간이동하면 끝)
        # 6을 2로 나누면 3
        if n % 2 == 0:
            n //= 2
        # 3의 위치로 가기 위해서는 한 칸 점프해서 가야함
        else:
            n -= 1
            ans += 1

    return ans