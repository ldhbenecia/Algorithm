def translate(n, k):
    trans_num = ''
    
    while n > 0:
        trans_num += str(n % k)
        n //= k

    return trans_num[::-1]

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    trans_num = translate(n, k)
    nums = trans_num.split('0')
    
    for i in nums:
        if i and is_prime(int(i)):
            answer += 1
    
    return answer