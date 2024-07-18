def solution(dirs):  
    dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
    dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
    
    visited = set()
    x, y = 0, 0
    
    for i in dirs:
        nx = x + dx[i]
        ny = y + dy[i]
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.add(((x, y), (nx, ny)))
            visited.add(((nx, ny), (x, y)))
            x, y = nx, ny
    
    return len(visited) // 2