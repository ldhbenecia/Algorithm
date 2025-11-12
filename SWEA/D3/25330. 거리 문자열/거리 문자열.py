T = int(input())

for _ in range(T):
    S = list(map(int, input()))

    # 존재하면 2개가 등장하는지
    # 두 숫자 사이에 있는 숫자의 개수가 그 두 숫자 개수인지 -> 1 3 1 -> 1 1 사이에 1개 있어야함
    dic = {}
    for i in S:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    # 2개가 등장하는 지 확인
    isValid = False
    for k, v in dic.items():
        if v != 2:
            print("no")
            isValid = True
            break
    if isValid:
        continue

    flag = True
    first_pos = {}
    for i in range(len(S)):
        if S[i] not in first_pos:
            # 제일 먼저 온 인덱스 구하기
            first_pos[S[i]] = i
        else:  # 이미 있는 수면
            first = first_pos[S[i]]

            # 131003이면 first_pos[1] = 0, first = 0, diff = 2 - 0 - 1 = 1
            diff = i - first - 1
            if diff != S[i]:
                flag = False
                break

    if not flag:
        print("no")
    else:
        print("yes")
