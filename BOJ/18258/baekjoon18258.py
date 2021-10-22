import sys
from collections import deque

n = int(sys.stdin.readline())
de = deque([])


def push(x):
    de.append(x)

def pop():
    if not de:
        return -1
    return de.popleft()

def size():
    return len(de)

def empty():
    if not de:
        return 1
    return 0

def front():
    if not de:
        return -1
    return de[0]

def back():
    if not de:
        return -1
    return de[-1]


for _ in range(n):
    num = sys.stdin.readline().split()

    if 'push' in num:
        push(num[1])
    elif 'front' in num:
        print(front())
    elif 'back' in num:
        print(back())
    elif 'size' in num:
        print(size())
    elif 'empty' in num:
        print(empty())
    else:
        print(pop())
