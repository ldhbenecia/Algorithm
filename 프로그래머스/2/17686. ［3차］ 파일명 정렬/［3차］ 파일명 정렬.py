def solution(files):
    answer = []
    HEAD = ''
    NUMBER = ''
    TAIL = ''
    for file in files:
        for i in range(len(file)):
            if file[i].isnumeric():
                HEAD = file[:i]
                NUMBER = file[i:]
                for j in range(len(NUMBER)):
                    if not NUMBER[j].isnumeric():
                        TAIL = NUMBER[j:]
                        NUMBER = NUMBER[:j]
                        break
                answer.append([HEAD, NUMBER, TAIL])
                HEAD, NUMBER, TAIL = '', '', ''
                break

    # 대소문자 구분 x, NUBMER순으로 정렬           
    answer.sort(key=lambda x:(x[0].lower(), int(x[1])))
    return [''.join(i) for i in answer]
