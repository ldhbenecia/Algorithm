def solution(array, commands):
    answer = []
    
    for i in range(len(commands)):
        start = commands[i][0]
        end = commands[i][1]
        target = commands[i][2] - 1
        section = array[start-1:end]
        section.sort()
        answer.append(section[target])
        
    return answer