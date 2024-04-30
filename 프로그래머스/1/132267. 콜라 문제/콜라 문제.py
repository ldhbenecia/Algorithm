def solution(a, b, n):
    answer = 0
    save = 0
    
    while n >= a:
        answer += (n // a) * b
        save = n % a
        n = save + (n // a) * b
        
    return answer
