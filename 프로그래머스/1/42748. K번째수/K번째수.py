def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        section = sorted(array[i-1:j])
        answer.append(section[k-1])

    return answer