def solution(operations):
    answer = []
    result = []
    
    for operate in operations:
        command, value = operate.split()
        value = int(value)
        
        if command == "I":
            answer.append(value)
        if command == "D":
            if answer and value == 1:
                max_value = max(answer)
                answer.remove(max_value)
            if answer and value == -1:
                min_value = min(answer)
                answer.remove(min_value)
    
    if not answer:
        result = [0, 0]
    else:
        max_value = max(answer)
        min_value = min(answer)
        result.append(max_value)
        result.append(min_value)
        
    return result