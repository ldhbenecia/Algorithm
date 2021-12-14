t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    result = pow(a, b, 10)
    if not result:
        print(result + 10) # 10 % 10 = 0 이므로 10이 나오게끔 출력
    else:
        print(result)