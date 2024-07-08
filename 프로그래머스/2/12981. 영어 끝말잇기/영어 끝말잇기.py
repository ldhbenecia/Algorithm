def solution(n, words):
    answer = []
    
    stack = []
    for i in range(len(words)):
        # 같은 말이 또 나왔을 경우
        if stack and words[i] in stack:
            a = (i % n) + 1  # 탈락하는 번호
            b = (i // n) + 1 # 몇번째에서 탈락
            answer = [a, b]
            break
        
        # 이전 말의 끝말과 동일하지 않을 경우
        if stack and words[i][0] != stack[-1][-1]:
            a = (i % n) + 1  # 탈락하는 번호
            b = (i // n) + 1 # 몇번째에서 탈락
            answer = [a, b]
            break
            
        stack.append(words[i])
    
    # 이외에 대한 처리
    if not answer:
        answer = [0, 0]

    return answer
