def solution(s):
    answer = 1001
    
    for i in range(1, len(s) + 1):
        result = ''
        count = 1
        prev = s[:i]
        for j in range(i, len(s) + i, i):
            if prev == s[j:j + i]:
                count += 1
            else:
                if count >= 2:
                    result += str(count) + prev
                else:
                    result += prev
            
                prev = s[j:j + i]
                count = 1
        
        answer = min(len(result), answer)
    return answer