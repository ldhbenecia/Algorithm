from collections import deque

def bfs(begin, target, words):
    queue = deque([(begin, 0)])
    
    while queue:
        v, idx = queue.popleft()
        #print(v, idx)
        
        if v == target:
            return idx
        
        for i in words:
            cnt = 0
            for j in range(len(v)):
                if v[j] != i[j]:
                    cnt += 1
                    
            if cnt == 1:
                queue.append([i, idx + 1])

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    return bfs(begin, target, words)