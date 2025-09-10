import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    arr = input().strip()
    if n == 0:
        queue = deque()
    else:
        queue = deque(map(int, arr[1:-1].split(",")))

    rev = False
    error = False
    for c in p:
        if c == "R":
            rev = not rev  # True, False 전환
        elif c == "D":
            if not queue:
                print("error")
                error = True
                break
            if rev:  # 반대방향이면 뒤에꺼 빼기
                queue.pop()
            else:  # 반대 아니면 앞에꺼 뺴기
                queue.popleft()

    if not error:
        if rev:
            queue.reverse()
        print("[" + ",".join(map(str, queue)) + "]")
