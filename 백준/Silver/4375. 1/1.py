while True:
    try:
        n = int(input())
    except:
        break

    num = '1'
    while True:
        if int(num) % n == 0:
            break
        else:
            num += '1'

    print(len(num))
