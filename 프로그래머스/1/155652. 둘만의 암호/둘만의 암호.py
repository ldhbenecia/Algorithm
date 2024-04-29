def solution(s, skip, index):
    answer = ''
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    
    for i in skip:
        alphabet.remove(i)
    for i in s:
        change = alphabet.index(i) + index
        if change >= len(alphabet):
            a = change % len(alphabet)
            answer += alphabet[a]
        else:
            answer += alphabet[change]

    return answer