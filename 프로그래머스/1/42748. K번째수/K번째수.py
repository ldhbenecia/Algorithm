def solution(array, commands):
    answer = []
    result = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        answer = sorted(array[i-1:j])
        result.append(answer[k-1])

    return result