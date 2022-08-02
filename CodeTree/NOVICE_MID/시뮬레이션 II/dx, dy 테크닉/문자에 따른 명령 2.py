a = input()

dir_num = 3
x, y = 0, 0

# 동남서북
# 0 1 2 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 동서남북으로 하였으나 그렇게 하면 L 입력시 북에서 서로 갈때 3에서 1로 -1만큼 빠지게 되며 간결하지가 않아서
# 동남서북으로 설정

#F는 한칸 이동

for i in a:
    if i == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif i == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)