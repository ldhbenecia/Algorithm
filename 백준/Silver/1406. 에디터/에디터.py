import sys

input = sys.stdin.readline

s = list(input().rstrip())
m = int(input())

left = s
right = []

for _ in range(m):
    command = input().split()

    if command[0] == "P":
        left.append(command[1])

    elif command[0] == "L":
        if left:
            right.append(left.pop())

    elif command[0] == "D":
        if right:
            left.append(right.pop())

    else:
        if left:
            left.pop()

print("".join(left + right[::-1]))

"""
[abcd] cursor []
[abcdx] cursor []
[abcd] cursor [x]
[abcdy] cursor [x]
"""
