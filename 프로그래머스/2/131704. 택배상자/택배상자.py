def solution(order):
    answer = 0
    
    stack = [] # 보조 컨테이너 벨트
    length = len(order)
    current, num = 0, 1
    
    while current < length:
        if order[current] > num:
            stack.append(num)
            num += 1
            
        elif order[current] == num:
            print(stack, order[current])
            break
        

    
    return answer
