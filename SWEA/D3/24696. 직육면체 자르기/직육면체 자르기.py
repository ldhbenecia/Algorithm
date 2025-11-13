T = int(input())

for _ in range(T):
    A, B, C = map(int, input().split())

    if A % 2 == 1 and B % 2 == 1 and C % 2 == 1:
        print(2)  # 다현
    else:
        print(1)  # 나연
