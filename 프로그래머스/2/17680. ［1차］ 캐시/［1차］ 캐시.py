from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    
    for i in cities:
        i = i.upper()
        if i in cache:
            answer += 1
            cache.remove(i)
            cache.append(i)
        else:
            answer += 5
            if cacheSize > 0:
                if len(cache) >= cacheSize:
                    cache.popleft()
                cache.append(i)
            
    return answer

# cache hit: 메모리가 캐시에 있는 경우
# cache miss: 메모리가 캐시에 존재하지 않는 경우