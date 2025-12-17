def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    
    left = 0
    right = 0
    while left < len(A) and right < len(B):
        if A[left] < B[right]:
            answer += 1
            left += 1
            
        right += 1
    
    return answer