gather = ['a', 'e', 'i', 'o', 'u']

while True:
    word = input().lower()

    if word == 'end':
        exit()

    valid = True
    # 모음 하나를 포함 여부
    check = 0
    for i in word:
        if i in gather:
            check += 1
    if check == 0:    
        valid = False

    # 모음 혹은 자음이 3개 연속으로 오는지
    gather_cnt = 0
    consonant_cnt = 0
    for i in word:
        if i in gather:
            gather_cnt += 1
            consonant_cnt = 0
        else:
            consonant_cnt += 1
            gather_cnt = 0

        if gather_cnt >= 3 or consonant_cnt >= 3:
            valid = False
            break

    # 같은 글자가 연속으로 두번 오면 안되나 ee, oo는 허용
    for i in range(1, len(word)):
        if word[i] == word[i - 1] and word[i] not in ['e', 'o']:
            valid = False

    if valid:
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
