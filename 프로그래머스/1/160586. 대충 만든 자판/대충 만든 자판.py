def solution(keymap, targets):
    answer = []
    key_dict = {}
    
    # 최소 클릭 횟수 딕셔너리 저장
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            char = keymap[i][j]
            if char not in key_dict:
                key_dict[char] = j + 1
            else:
                key_dict[char] = min(key_dict[char], j + 1)
    
    for target in targets:
        time = 0
        for i in target:
            if i in key_dict:
                time += key_dict[i]
            else:
                time = -1
                break
        answer.append(time)
        
    return answer

# 설계
# key맵의 각각 순서대로 인덱스를 구함
# ex: ABACD 1 2 3 4 5, BCEFD 1 2 3 4 5
# ABCD= A: 1 / B: 2, 1 / C: 4, 2 / D: 5, 5
# 여기서 최소값들 뽑아서 합산하면 됨