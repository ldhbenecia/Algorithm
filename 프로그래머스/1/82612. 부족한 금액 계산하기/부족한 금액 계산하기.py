def solution(price, money, count):
    answer = 0
    fee = 0
    
    for i in range(1, count + 1):
        fee += price * i
    
    if fee - money > 0:
        answer = fee - money
    else:
        answer = 0
    
    return answer