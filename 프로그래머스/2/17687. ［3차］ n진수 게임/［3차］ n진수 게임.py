def get_n(n):
    digits = "0123456789ABCDEF"
    lst = []
    
    for i in range(100000):
        num = i
        temp = ''
        if num == 0:
            temp = '0'
        else:
            while num > 0:
                temp = digits[num % n] + temp
                num //= n
        lst.append(temp)
            
    full_string = ''.join(lst)
    return full_string

def solution(n, t, m, p):
    answer = ''
    
    n_string = get_n(n)
    for i in range(p - 1, len(n_string), m):
        answer += n_string[i]
        
    answer = answer[:t]
    
    return answer