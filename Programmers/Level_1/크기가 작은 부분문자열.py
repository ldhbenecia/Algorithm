def solution(t, p): # 문자열로 숫자가 들어옴
    answer = 0
    
    # 몇자리 수인지
    len_t = len(t)
    len_p = len(p)
    
    for i in range(len_t-len_p+1):
        if int(t[i:i+len_p]) <= int(p):
            answer += 1
    
    return answer

# 3141592 271 -> 141 159해서 2개
# 314 141 415 159 592 총 7개중에서 3개씩 쪼개면 5개가 나옴
# 7 - 3 = 4인데 5개가 나와야됨

# 5 0 0 2 2 0 8 3 9 8 7 8 총 12개 중에서 8개
# 12 - 1 = 11인데 12개가 나와야됨

# 10 02 20 03 총 5개 중에서 4개로 쪼개짐
# 5 - 2 = 3인데 4개가 나와야됨