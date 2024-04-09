def solution(n, lost, reserve):
    
    # 체육복 있는 학생
    s = set(lost) & set(reserve)
    
    # 도난 당해서 체육복 없는 학생
    plz_safe = set(lost) - s
    
    # 도난 당했으나 여벌 체육복을 가지고 있는 학생
    safe = set(reserve) - s
    
    for i in safe:
        if i - 1 in plz_safe:
            plz_safe.remove(i - 1)
        elif i + 1 in plz_safe:
            plz_safe.remove(i + 1)
        
    return n - len(plz_safe)