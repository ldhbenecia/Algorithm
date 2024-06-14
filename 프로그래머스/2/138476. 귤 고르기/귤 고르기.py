def solution(k, tangerine):
    answer = 0
    dic = {}
    
    for i in tangerine:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    dic = sorted(dic.items(), key = lambda x:x[1], reverse=True)
    
    # 개수가 적은 귤을 제외하는 것이 아닌 개수가 많은 것들을 추출
    # k = 6, 3, 2, 5번 귤 2개씩 추출 -> 3 종류
    for size, cnt in dic:
        k -= cnt
        answer += 1
        
        if k <= 0:
            break
    
    return answer