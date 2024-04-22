alphabet_list = ['A', 'E', 'I', 'O', 'U']
idx, result = 0, 0

def dfs(cnt, alphabet, word):
    global idx, result
    
    if alphabet == word:
        result = idx
        return
    
    if cnt == 5:
        return
    
    for i in range(5):
        idx += 1
        dfs(cnt + 1, alphabet + alphabet_list[i], word)

def solution(word):
    global result
    
    dfs(0, '', word)
    return result
