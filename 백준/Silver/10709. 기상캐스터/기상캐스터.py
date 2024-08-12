h, w = map(int, input().split())
graph = [input() for _ in range(h)]

result = []
for i in range(h):
    temp = []
    count = 0
    for j in range(w):
        if graph[i][j] == 'c':
            temp.append(0)
            count = 0
            continue
        if 0 in temp:
            count += 1
            temp.append(count)
        if not temp and graph[i][j] != 'c':
            temp.append(-1)
            continue
        if temp[-1] == -1 and graph[i][j] != 'c':
            temp.append(-1)
            continue
    
    result.append(temp)
    
for i in result:
    print(*i)