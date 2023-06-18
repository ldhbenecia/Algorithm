'''
n = int(input())
move = input().split()

x, y = 1, 1
dx = [0, 0, -1 ,1]
dy = [-1, 1, 0, 0]

move_type = ['L', 'R', 'U', 'D']

for i in move:
    for j in range(len(move_type)):
        if i == move_type[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    x, y = nx, ny
    
print(x, y)
'''

n = int(input())
command = input().split()

x, y = 1, 1 # 초기 좌표

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in command:
    if i == "L":
        nx = x + dx[2]
        ny = y + dy[2]
        
    if i == "R":
        nx = x + dx[3]
        ny = y + dy[3]
        
    if i == "U":
        nx = x + dx[0]
        ny = y + dy[0]
        
    if i == "D":
        nx = x + dx[1]
        ny = y + dy[1]
        
    # 맵을 뚫었을 때
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue # 무시하고 진행
    
    x, y = nx, ny
    
print(x, y)


