def solution(food):
    answer = []
    result = []
    for i in range(1, len(food)):
        answer.append(str(i) * (food[i] // 2))
        
    reverse_answer = answer[::-1]
    result = (''.join(answer) + "0" + ''.join(reverse_answer))
    
    return result


# 총 음식 13개
# 가운데 물 두면 12개
# 각각 6개
# 3 4 6개 있으므로 
# 1 22 333 0 333 22 1

# 총 음식 10개 준비되어있음
# 가운데 물 두면 9개이기 때문에 8개
# 각각 4개
# 7 1 2개
# 111 3 0 3 111