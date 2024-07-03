def binary_converter(n):
    temp = ''
    
    while n:
        temp += str(n % 2)
        n //= 2
    
    return temp[::-1]

def solution(n):
    answer = 0
    
    binary_n = binary_converter(n)
    temp = n + 1
    
    while True:
        if binary_converter(temp).count('1') == binary_n.count('1'):
            answer = temp
            break
        
        temp += 1
    
    return answer