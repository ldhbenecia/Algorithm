def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        a = bin(arr1[i])[2:].zfill(n)
        b = bin(arr2[i])[2:].zfill(n)
        row = ''
        for j in range(n):
            if a[j] == '0' and b[j] == '0':
                row += ' '
            else:
                row += '#'
        answer.append(row)
    
    return answer
