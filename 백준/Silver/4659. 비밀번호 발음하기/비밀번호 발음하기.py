moem = ["a", "e", "i", "o", "u"]

while True:
    t = input()

    if t == "end":
        break

    # 모음을 포함하는가?
    hasMoem = False
    for i in t:
        if i in moem:
            hasMoem = True
            break

    if hasMoem == False:
        print(f"<{t}> is not acceptable.")
        continue

    # 모음이 3개 혹은 자음이 3개 연속으로 오는가?
    hasSequence = False
    for i in range(len(t) - 2):
        if t[i] in moem and t[i + 1] in moem and t[i + 2] in moem:
            hasSequence = True
            break
        elif not t[i] in moem and not t[i + 1] in moem and not t[i + 2] in moem:
            hasSequence = True
            break

    if hasSequence == True:
        print(f"<{t}> is not acceptable.")
        continue

    # 같은 글자가 연속으로 2개인지 체크, 'e', 'o'는 허용
    isCheck = False
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            if t[i] == "e" or t[i] == "o":
                continue
            isCheck = True

    if isCheck == True:
        print(f"<{t}> is not acceptable.")
        continue

    print(f"<{t}> is acceptable.")
    continue
