n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

#상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def answer_cnt(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and graph[nx][ny] == 1:
            cnt += 1
    return cnt


result = 0
for i in range(n):
    for j in range(n):
        if answer_cnt(i, j) >= 3:
            result += 1

print(result)


'''
n = int(input())

# grid = [
#     [0, 1, 0, 1],
#     [0, 0, 1, 1],
#     [0, 1, 0, 1],
#     [0, 0, 1, 0]
# ]

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# (x, y) 위치를 기점으로 인접한 칸에 있는 숫자 1의 
# 개수를 세줍니다.
ans = 0
for x in range(n):
    for y in range(n):
        dxs = [ 0, 0, -1, 1]
        dys = [-1, 1,  0, 0]

        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and grid[nx][ny] == 1:
                cnt += 1
        
        # (x, y)와 인접한 칸에 있는 숫자 1의 개수
        if cnt >= 3:
            ans += 1

print(ans)
'''