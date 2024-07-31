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
                temp += digits[num % n]
                num //= n
        temp = temp[::-1]
        lst.extend(temp)
        
    return lst

def solution(n, t, m, p):
    answer = ''
    
    n_lst = get_n(n)
    for i in range(p - 1, len(n_lst), m):
        answer += n_lst[i]
        
    answer = answer[:t]
    
    return answer