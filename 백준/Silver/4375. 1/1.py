while True:
    try:
        n = int(input())
    except:
        break

    num = 1
    cnt = 1  # 자릿수

    while True:
        if num % n == 0:
            print(cnt)
            break

        num = num * 10 + 1
        cnt += 1
