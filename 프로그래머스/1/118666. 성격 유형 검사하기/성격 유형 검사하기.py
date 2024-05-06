def solution(survey, choices):
    answer = ''
    personality = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        bad = survey[i][0]
        good = survey[i][1]
        
        if choices[i] == 1:
            personality[bad] += 3
        if choices[i] == 2:
            personality[bad] += 2
        if choices[i] == 3:
            personality[bad] += 1
        if choices[i] == 4:
            pass
        if choices[i] == 5:
            personality[good] += 1
        if choices[i] == 6:
            personality[good] += 2
        if choices[i] == 7:
            personality[good] += 3
    
    print(personality['R'])
    if personality['R'] >= personality['T']:
        answer = answer + 'R'
    elif personality['R'] < personality['T']:
        answer = answer + 'T'
    
    if personality['C'] >= personality['F']:
        answer = answer + 'C'
    elif personality['C'] < personality['F']:
        answer = answer + 'F'
        
    if personality['J'] >= personality['M']:
        answer = answer + 'J'
    elif personality['J'] < personality['M']:
        answer = answer + 'M'
        
    if personality['A'] >= personality['N']:
        answer = answer + 'A'
    elif personality['A'] < personality['N']:
        answer = answer + 'N'
    
    return answer
