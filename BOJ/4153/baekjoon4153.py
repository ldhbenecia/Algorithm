while True:
    w, h, p = map(int,input().split())
    if w == h == p == 0:
        break
    
    # 리스트를 만들어 정렬을 해주는 이유는 정렬을 해서 크기순으로 인덱스 제일 뒷 값이 제일 큰 값이기 때문
    list = [w, h, p]
    list.sort()

    if list[0] ** 2 + list[1] **2 == list[2] ** 2:
        print("right")
    else:
        print("wrong")