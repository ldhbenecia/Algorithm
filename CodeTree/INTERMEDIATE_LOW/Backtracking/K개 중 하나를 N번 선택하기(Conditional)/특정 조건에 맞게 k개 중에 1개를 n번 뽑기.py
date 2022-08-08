k, n = tuple(map(int, input().split()))
answer = []

def print_answer():
    for i in answer:
        print(i, end = ' ')
    print()

def select(cnt):
    if cnt == n:
        print_answer()
        return

    for i in range(1, k+1):
        if cnt >= 2 and answer[-1] == i and answer[-2] == i:
            continue
        else:
            answer.append(i)
            select(cnt+1)
            answer.pop()

select(0)