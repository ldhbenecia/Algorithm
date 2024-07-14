def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 두 글자씩 끊어서 다중집합 원소 저장
    str1_lst = [str1[i] + str1[i+1] for i in range(len(str1) - 1)]
    str2_lst = [str2[i] + str2[i+1] for i in range(len(str2) - 1)]
    
    # 영문자 제외 공백, 숫자, 특수 문자가 들어있는 경우 제거
    str1_lst = [item for item in str1_lst if item.isalpha()]
    str2_lst = [item for item in str2_lst if item.isalpha()]    
    
    # 교집합, 합집합 크기
    intersection, union = 0, 0
    
    for i in set(str1_lst).union(set(str2_lst)):
        intersection += min(str1_lst.count(i), str2_lst.count(i))
        union += max(str1_lst.count(i), str2_lst.count(i))
    
    if union == 0:
        answer = 1
        
    if intersection == 0 and union == 0:
        answer = 65536
    else:
        answer = intersection / union * 65536
    
    return int(answer)
