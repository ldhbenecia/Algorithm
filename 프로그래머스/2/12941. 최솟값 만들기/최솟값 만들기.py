def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)
    i = 0
    while True:
        if i == len(A):
            break
            
        answer += A[i] * B[i]
        i += 1
            
    return answer