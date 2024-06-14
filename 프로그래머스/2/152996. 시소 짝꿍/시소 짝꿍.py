from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    # 같은 수가 2개 이상인 경우 1:1 존재
    for i, cnt in counter.items():
        if cnt > 1:
            answer += cnt * (cnt - 1) // 2 # 수식
    
    weights = set(weights)
            
    for i in weights:
        if i * 1/2 in weights:
            answer += counter[i*1/2] * counter[i] # 해당 비율에 속하는 무게가 몇개인지 더하기
        if i * 2/3 in weights:
            answer += counter[i*2/3] * counter[i]
        if i * 3/4 in weights:
            answer += counter[i*3/4] * counter[i]
        
    return answer