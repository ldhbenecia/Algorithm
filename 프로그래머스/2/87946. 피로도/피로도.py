from itertools import permutations

def solution(k, dungeons):
    answer = -1
    dungeons_len = len(dungeons)
    
    for per in permutations(dungeons, dungeons_len):
        cnt = 0
        hp = k
        for i, j in per:
            if hp >= i:
                hp -= j
                cnt += 1
                
            if cnt >= answer:
                answer = cnt
    
    return answer